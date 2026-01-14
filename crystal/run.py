import os
import sys

# Add the parent directory to the Python path to allow for absolute imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from crystal.core.dashboard import app
from crystal.core.socket_manager import socketio, init_socketio
from crystal.utils.logger import get_logger
from crystal.utils.banner import print_banner
from crystal.utils.db import init_db

# Initialize SocketIO with the Flask app
init_socketio(app)
logger = get_logger()

# Print a random startup banner
print_banner()

# Initialize the database
logger.info("Initializing the database...")
init_db()
logger.info("Database initialized successfully.")

# This is the entry point for Gunicorn
# Gunicorn will look for the 'app' object in this module.
if __name__ == '__main__':
    # This block is now only for direct execution (e.g., for local testing without Gunicorn)
    logger.info("Starting Crystal server with Flask's development server.")
    socketio.run(app, host='0.0.0.0', port=5000, debug=True, allow_unsafe_werkzeug=True)
