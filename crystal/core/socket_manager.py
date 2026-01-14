from flask_socketio import SocketIO

# Initialize a SocketIO instance.
# This will be used to manage real-time, bidirectional communication
# between the server and the clients (the web dashboard).
socketio = SocketIO()

def init_socketio(app):
    """
    Initializes the SocketIO server with the Flask application.
    This function links the SocketIO instance to the Flask app, enabling
    WebSocket functionality.

    Args:
        app: The Flask application instance.
    """
    socketio.init_app(app)

# Example WebSocket event handlers can be defined below.
# These handlers will manage incoming WebSocket messages from the client.

@socketio.on('connect')
def handle_connect():
    """
    Handles a new client connection.
    This is a built-in event that fires whenever a new client establishes a
    WebSocket connection with the server.
    """
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    """
    Handles a client disconnection.
    This is a built-in event that fires whenever a client disconnects.
    """
    print('Client disconnected')

@socketio.on('message')
def handle_message(data):
    """
    Example handler for a custom 'message' event.
    This function will be called when a client sends a message on the
    'message' channel.

    Args:
        data: The data sent by the client.
    """
    print('received message: ' + str(data))
    # We can broadcast the message back to all clients or a specific one.
    socketio.emit('response', {'data': 'Message received!'})
