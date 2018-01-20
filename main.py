from flask import Flask, render_template, request, redirect, session
import re, sys

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/add", methods = ['POST'])
def add():
    session.pop('errors', None)
    errors = []
    try:
        name = request.form['name']
        lastname = request.form['lastname']
        email = request.form['email']
        phone = request.form['phone']
        phone_type = request.form['phone_type']
        address = request.form['address']

        errors = validate(name, email, phone)
        session['errors'] = errors

        if len(errors) == 0:
            n = 1
            #aqui lo agrega a la base de datos
            
    except:
        errors.append("Something happened in server :(")
    return redirect("/", code=302)

@app.route("/update", methods = ['POST'])
def update():
    session.pop('errors', None)
    errors = []
    try:
        id_user = int(request.form['id'])
        name = request.form['name']
        lastname = request.form['lastname']
        email = request.form['email']
        phone = request.form['phone']
        phone_type = request.form['phone_type']
        address = request.form['address']

        errors = validate(name, email, phone)
        session['errors'] = errors

        if len(errors) == 0:
            n = 1
            #aqui le hace update a la base de datos
            
    except:
        errors.append("Something happened in server : "+sys.exc_info()[0])
        
    return redirect("/", code=302)

def validate(name, email, phone):
    errors = []
    if name=="":
        errors.append("Invalid name")
    if phone=="":
        errors.append("Invalid phone")
    if not re.match("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        errors.append("Invalid email format")
    return errors

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug = True, port = 8080)
    
