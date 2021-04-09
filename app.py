# Import Dependencies
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Set database engine
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()

Base.prepare(engine, reflect=True)

# Set the variables for classes
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link
session = Session(engine)

# Define Flask app
app = Flask(__name__)

# Create the Welcome route
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')