from flask import Flask,render_template,request
import mysql.connector
user_dict={'admin':'1234','user':'5678'}
conn = mysql.connector.connect(host='localhost',user='root',password='',database='blood')
mycursor=conn.cursor()
#create a flask application
app = Flask(__name__)

#Define the route 

@app.route('/')
def hello():
    return render_template('home.html')
@app.route('/donor')
def donors():
    return render_template('bloodreg.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/admin',methods=['POST'])
def admin():
    uname=request.form['username']
    pwd=request.form['password']

    if uname not in user_dict:
        return render_template('login.html',msg='Invalid User')
    elif user_dict[uname] != pwd:
        return render_template('login.html',msg='Invalid Password')
    else:
        return render_template('admin.html')
@app.route('/view')
def view():
    query="SELECT * FROM donors"
    mycursor.execute(query)
    data=mycursor.fetchall()
    return render_template('view.html',sqldata=data)

@app.route('/search')
def searchpage():
    return render_template('search.html')
@app.route('/registration')
def registration():
    return render_template('bloodreg.html')
@app.route('/searchresult',methods=['POST'])
def search():
    sas = request.form['a7']
    query="SELECT * FROM donors WHERE City="+sas
    mycursor.execute(query)
    data=mycursor.fetchall()
    return render_template('view.html',sqldata=data)
    
@app.route('/deleteresult',methods=['POST'])
def deleteresult():
    empid = request.form['emp_id']
    query="SELECT * FROM donors WHERE ID="+idd
    mycursor.execute(query)
    data=mycursor.fetchall()
    return render_template('view.html',sqldata=data)

@app.route('/regist',methods=['POST'])
def regist():
    a = request.form['a9']
    n = request.form['a1']
    c = request.form['a2']
    f = request.form['a3']
    e = request.form['a4']
    g = request.form['a5']
    h = request.form['a6']
    i = request.form['a7']
    query = "INSERT INTO donors(id,full_name,date_of_birth,blood_group,last_donation_date,Phone_number,Address,City) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    data = (a,n,c,f,e,g,h,i)
    mycursor.execute(query,data)
    conn.commit()
    return render_template('bloodreg.html',msgdata='Added Successfully')
@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')
@app.route('/delete')
def delete():
    return render_template('delete.html')

#Run the flask app
if __name__=='__main__':
    app.run(port=5001,debug = True)