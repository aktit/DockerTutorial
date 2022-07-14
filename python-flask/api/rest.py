from concurrent.futures import process
from flask import Flask, jsonify, redirect
from flaskext.mysql import MySQL
app = Flask(__name__)

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'testing'
app.config['MYSQL_DATABASE_HOST'] = 'mysql'

mysql.init_app(app)

try: 
    mysql.connect()
    
    @app.route('/', methods=['GET'])
    def index():
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("select * from employees")
        a = cursor.fetchall()
        conn.close()
        return jsonify(a)

    @app.route('/post/<first_name>/<last_name>')
    def post(first_name, last_name, methods=['POST']):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('''insert into employees(first_name,last_name) values(%s,%s)''', (first_name, last_name))
        conn.commit()
        conn.close()
        return redirect("/")

    @app.route('/put/<emp_no>/<first_name>/<last_name>')
    def put(first_name, last_name, emp_no, methods=['PUT']):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('''update employees set first_name = %s, last_name = %s where emp_no = %s''', 
        (first_name, last_name, emp_no))
        conn.commit()
        conn.close()
        return redirect("/")

    @app.route('/delete/<emp_no>')
    def delete(emp_no, methods=['DELETE']):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('''delete from employees where emp_no = %s''', 
        (emp_no))
        conn.commit()
        conn.close()
        return redirect("/")
    app.run(host='0.0.0.0',port=5000)
    

except:
    @app.route("/")
    def hello():
        return "DB is not working properly! Please check the DB and restart the app again!"
    app.run(host='0.0.0.0',port=5000)
