import socket
import threading
from crystal.utils.logger import get_logger

logger = get_logger()

class ListenerHandler:
    """
    Handles incoming reverse shell connections.
    Manages multiple concurrent sessions and provides a way to interact with them.
    """
    def __init__(self):
        self.sessions = {}
        self.next_session_id = 1
        self.server_socket = None
        self.is_running = False

    def start_listener(self, host, port):
        """
        Starts a new listener on the specified host and port.

        Args:
            host (str): The host IP address to bind the listener to.
            port (int): The port to listen on.
        """
        if self.is_running:
            logger.warning("A listener is already running.")
            return

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            self.server_socket.bind((host, port))
            self.server_socket.listen(5)
            self.is_running = True
            logger.info(f"Listener started on {host}:{port}")

            # Start a thread to accept incoming connections
            accept_thread = threading.Thread(target=self._accept_connections)
            accept_thread.daemon = True
            accept_thread.start()
        except Exception as e:
            logger.error(f"Failed to start listener on {host}:{port}: {e}")
            self.is_running = False

    def _accept_connections(self):
        """
        Private method to run in a thread and accept incoming connections.
        """
        logger.info(f"Accept loop started. is_running = {self.is_running}")
        while self.is_running:
            try:
                # This is a blocking call. The thread will pause here until a connection is made.
                conn, addr = self.server_socket.accept()

                # If we get past the accept call, a connection was made.
                logger.info(f"--- !!! CONNECTION ACCEPTED !!! --- from {addr}")

                session_id = self.next_session_id
                self.next_session_id += 1

                session = {
                    'id': session_id,
                    'conn': conn,
                    'addr': addr,
                    'is_active': True
                }
                self.sessions[session_id] = session
                logger.info(f"New session created and stored with ID: {session_id}. Total sessions: {len(self.sessions)}")

            except socket.error as e:
                if self.is_running:
                    logger.error(f"Socket error in accept loop: {e}")
                # This is the expected way to exit the loop when stop_listener() is called.
                break
            except Exception as e:
                logger.error(f"An unexpected error occurred in accept loop: {e}")

        logger.info(f"Accept loop terminated. is_running = {self.is_running}")

    def stop_listener(self):
        """Stops the listener and closes all active sessions."""
        if not self.is_running:
            logger.warning("Listener is not currently running.")
            return

        self.is_running = False
        for session_id, session in self.sessions.items():
            if session['is_active']:
                try:
                    session['conn'].close()
                except socket.error:
                    pass # The connection might already be closed

        try:
            self.server_socket.close()
        except socket.error:
            pass

        self.sessions.clear()
        self.next_session_id = 1
        logger.info("Listener and all active sessions have been stopped.")

    def get_sessions(self):
        """Returns a list of active sessions."""
        return [
            {'id': s['id'], 'addr': f"{s['addr'][0]}:{s['addr'][1]}", 'is_active': s['is_active']}
            for s in self.sessions.values()
        ]

    def send_command(self, session_id, command):
        """Sends a command to a specific session and returns the output."""
        session = self.sessions.get(session_id)
        if not session or not session['is_active']:
            return "Error: Session not found or is inactive."

        try:
            # Add a newline to the command to ensure it's executed
            session['conn'].sendall((command + '\\n').encode('utf-8'))

            # This is a simplified receive logic. A more robust implementation
            # would handle larger outputs and timeouts.
            session['conn'].settimeout(2.0)
            response = session['conn'].recv(4096).decode('utf-8', 'ignore')
            return response
        except socket.timeout:
            return "Timeout: No response from the client."
        except socket.error as e:
            logger.error(f"Socket error with session {session_id}: {e}")
            session['is_active'] = False
            return "Error: Connection lost."

# This module is not meant to be run directly.
