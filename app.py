# Import the Flask dependency
from flask import Flask

# Create a new Flask instance
app = Flask(__name__)

# Create the route
@app.route('/')
def hello_world():
    return 'Hello world'