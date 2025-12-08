from flask import Flask, render_template
from .crystal_api import api_blueprint

# Note: The template_folder and static_folder paths are relative to the application's root path.
# When run.py (located in the 'crystal' directory) imports this module,
# Flask will correctly resolve these paths to 'crystal/templates' and 'crystal/static'.
app = Flask(__name__, template_folder='../templates', static_folder='../static')

# Register the API blueprint
app.register_blueprint(api_blueprint)

@app.route('/')
def index():
    """Serves the main dashboard page."""
    return render_template('index.html')

@app.route('/modules')
def modules():
    """Serves the modules page."""
    return render_template('modules.html')
