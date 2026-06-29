from flask import Flask

app = Flask(__name__)

from app import routes

# The routes handle the different URLs that the application supports. In Flask, handlers for the application routes are written as Python functions, called view functions.