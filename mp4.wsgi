import sys
import os

# Specify the Python path
sys.path.insert(0, '/var/www/html/mp4')

# Set the Flask app location
os.environ['FLASK_APP'] = 'mp4'

# Import the app
from mp4 import app as application
