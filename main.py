from flask import Flask, render_template, request, redirect, session
import re, sys
from flaskext.mysql import MySQL
from flask_sqlalchemy import SQLAlchemy

mysql = MySQL()

app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = 'sql3.freemysqlhosting.net'
app.config['MYSQL_DATABASE_USER'] = 'sql3216877'
app.config['MYSQL_DATABASE_PASSWORD'] = 'QwFHXgwK62'
app.config['MYSQL_DATABASE_DB'] = 'sql3216877'
app.config['MYSQL_DATABASE_PORT'] = 3306

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sql3216877:QwFHXgwK62@sql3.freemysqlhosting.net/sql3216877'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

mysql.init_app(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    phone_type = db.Column(db.String(10))
    address = db.Column(db.String(255))

@app.route("/")
def index():
    cur = mysql.get_db().cursor()
    cur.execute('''SELECT * FROM agenda''')
    rv = cur.fetchall()
    cur.close()
    return render_template('index.html', entries=rv)

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
            # n = 1
            #aqui lo agrega a la base de datos
            # cur = mysql.get_db().cursor()
            # cur.execute('''INSERT INTO agenda(id,name,lastname,email,phone,phone_type,address) VALUES(%d,%s,%s,%s,%s,%s,%s)''', (NULL,name,lastname,email,phone,phone_type,address))
            
            signature = Contact(name=name,lastname=lastname,email=email,phone=phone,phone_type=phone_type,address=address)
            db.session.add(signature)
                  
            
    except:
        errors.append("Something happened in server :(")
    
    
    db.session.commit() 
    #cur.close()
    #return render_template("index.html", name=name,lastname=lastname,email=email,phone=phone,phone_type=phone_type,address=address)
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

@app.route("/delete")
def delete():
    id_user = int(request.args.get("id","1"))
    return str(id_user)

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
