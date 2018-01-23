from flask import Flask, render_template, request, redirect, session, jsonify
import re, sys
from flaskext.mysql import MySQL

app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = 'sql3.freemysqlhosting.net'
app.config['MYSQL_DATABASE_USER'] = 'sql3216877'
app.config['MYSQL_DATABASE_PASSWORD'] = 'QwFHXgwK62'
app.config['MYSQL_DATABASE_DB'] = 'sql3216877'
app.config['MYSQL_DATABASE_PORT'] = 3306

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

mysql = MySQL(app)

add = False
update = False
delete = False

@app.route("/")
def index():
    session.pop('add', None)
    session.pop('update', None)
    session.pop('delete', None)
    cur = mysql.get_db().cursor()
    cur.execute('''SELECT * FROM agenda''')
    rv = cur.fetchall()
    cur.close()
    if add:
        n = 1
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
            cur = mysql.get_db().cursor()
            cur.execute('''INSERT INTO agenda(name,lastname,email,phone,phone_type,address) VALUES(%s,%s,%s,%s,%s,%s)''',(name,lastname,email,phone,phone_type,address))
            mysql.get_db().commit()
            
    except Exception as e:
        errors.append("Something happened in server :(... "+str(e))
    
    return redirect("/", code=302)

@app.route("/update", methods = ['POST'])
def update():
    session.pop('errors', None)
    errors = []
    try:
        id_user = request.form['id']
        name = request.form['name']
        lastname = request.form['lastname']
        email = request.form['email']
        phone = request.form['phone']
        phone_type = request.form['phone_type']
        address = request.form['address']

        errors = validate(name, email, phone)
        session['errors'] = errors

        if len(errors) == 0:
            cur = mysql.get_db().cursor()
            cur.execute('''UPDATE agenda SET name = %s, lastname = %s, email = %s, phone = %s, phone_type = %s, address = %s WHERE id = %s ''',(name,lastname,email,phone,phone_type,address, id_user))
            mysql.get_db().commit()
            
    except Exception as e:
        errors.append("Something happened in server :(... "+str(e))
        
    return redirect("/", code=302)

@app.route("/delete")
def delete():
    session.pop('errors', None)
    errors = []
    try:
        id_user = request.args.get("id","1")

        if len(errors) == 0:
            cur = mysql.get_db().cursor()
            cur.execute('''DELETE FROM agenda WHERE id = %s ''',(id_user))
            mysql.get_db().commit()
            
    except Exception as e:
        errors.append("Something happened in server :(... "+str(e))
        
    return redirect("/", code=302)

@app.route('/getrow')
def getrow():
    id_user = request.args.get("id","1")
    cur = mysql.get_db().cursor()
    cur.execute('''SELECT * FROM agenda WHERE id = %s''', (id_user))
    row = cur.fetchall()
    return jsonify(name=row[0][1],
                   lastname=row[0][2],
                   email=row[0][3],
                   phone = row[0][4],
                    phone_type = row[0][5],
                   address =row[0][6]
                  )


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
