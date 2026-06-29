from app import app
from flask import render_template

#the two  @app.route lines above the function are decorators, 
@app.route('/')
@app.route('/index')
def index():
    user = { 'username' : 'Miguel'}
    return render_template('index.html', title='Home', user=user)
    
#A decorator modifies the function that follows it. A common pattern with decorators is to use them to register functions as callbacks for certain events. In this case, the @app.route decorator creates an association between the URL given as an argument and the function. 