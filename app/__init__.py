from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes

# The routes handle the different URLs that the application supports. In Flask, handlers for the application routes are written as Python functions, called view functions.