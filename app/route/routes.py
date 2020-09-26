from app import app
from app.controllers import controllerRoute
from flask import render_template

@app.route('/ctr')
def testctr():
    return controllerRoute.fungsiController()

@app.route('/ctr/')
@app.route('/ctr/<parameter>')
def testctParameter(parameter="kosong"):
    return controllerRoute.fungsiControllerParameter(parameter)

@app.route('/')
def index():
    # return "Hello, World!"
    message_value = "Hello, World"
    return render_template('index.html',message_key=message_value)  

 
# @app.route('/users/')
# @app.route('/user/<name>') 
# @app.route('/user/')
# def tesParameter(name="kosong"): # 3 routes diatas, membaca satu def ini
#     return f"Hello,{name}!"

# @app.route('/users_coba/')
# @app.route('/users_coba/<name>')
# def tesParameter1(name="kosong"):# 2 routes diatas, membaca satu def ini
#     return f"coba,{name}!" 