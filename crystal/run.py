import os
import sys

# Add the parent directory to the Python path to allow for absolute imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from crystal.core.dashboard import app
from crystal.core.socket_manager import socketio, init_socketio

# Initialize SocketIO with the Flask app
init_socketio(app)

if __name__ == '__main__':
    """
    Main entry point for the Crystal application.
    This script starts the Flask-SocketIO development server.

    In a production environment, a more robust WSGI server like Gunicorn or uWSGI
    should be used.
    """
    # Configuration for the server
    HOST = '0.0.0.0'
    PORT = 5000
    DEBUG_MODE = True

    print(f"[*] Starting Crystal server at http://{HOST}:{PORT}")

    # Run the application using the SocketIO development server.
    # The debug mode will provide helpful error messages and automatically
    # reload the server when code changes are detected.
    socketio.run(app, host=HOST, port=PORT, debug=DEBUG_MODE, allow_unsafe_werkzeug=True)
