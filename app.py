from flask import Flask, render_template, request
print(__file__)

import os
project_dir = os.path.dirname(os.path.abspath(__file__))
myApp = Flask(__name__)
print(project_dir)

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))

myApp.config["SQLALCHEMY_DATABASE_URI"] = database_file
myApp.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False



db = SQLAlchemy(myApp)

#db.create_all()

class user(db.Model):
    name = db.Column(db.String(40), nullable=False)
    ffname = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    dob = db.Column(db.String(40), nullable=False)
    gender = db.Column(db.String(40), nullable=False)
    phonenum = db.Column(db.String(40), nullable=False)
    cnic = db.Column(db.String(40), nullable=False, primary_key = True)
    re = db.Column(db.String(40), nullable=False,)
    pp = db.Column(db.String(40), nullable=False)
    status= db.Column(db.String(40), nullable=False)
 

#db.create_all()

@myApp.route("/")
def hello():

    return render_template('index2.html')

@myApp.route("/users",methods=["GET", "POST"])
def harry():
    if request.method == "POST":
        user1 = user()
        user1.name = request.form['Username']
        user1.ffname = request.form['ffname']
        user1.email=request.form['email']
        user1.dob=request.form['dob']
        user1.gender=request.form['gender']
        user1.phonenum=request.form['phonenum']
        user1.cnic=request.form['cnic']
        user1.re = request.form['Re']
        user1.pp = request.form['pp']
        user1.status = request.form['status']

        db.session.add(user1)
        db.session.commit()
        myUsers = user.query.all()
    return render_template('users.html',users=myUsers)
    #return render_template('index2.html')


@myApp.route("/panel", methods=["POST", "GET"])
def harr():
        uname = request.form['uname']
        pwrd = request.form['password']
        re=request.form['re']
        user_found = user.query.filter_by(name=uname, pp=pwrd,re=re).first()
        #print(user_found)
        if user_found:
            if re=="Teacher":
                return render_template('u.html') 
            elif  re=="Student":
               
                return render_template('u2.html', users=myUsers)
            elif re=="Admin":
                myUsers = user.query.all()
                return render_template('users.html', users=myUsers)  
            else:
                return "soryy" 
        else:
            return render_template('index2.html')


@myApp.route("/index2")
def harris():
    name = "rohans"
    return render_template('index2.html', name4= name)
@myApp.route("/regg")
def waheed():
    name = "rohans"
    return render_template('reg.html', name4= name)
@myApp.route("/logout")
def logout():
    name = "log"
    return render_template('index2.html', name124= name)

@myApp.route('/delete', methods=["POST"])
def delete_user():
    
        user_name = request.form['target_user']

        user_found = user.query.filter_by(name=user_name).first()

        db.session.delete(user_found)
        db.session.commit()
        myUsers = user.query.all()
@myApp.route("/edit",methods=["GET", "POST"] )
def edit():
    user_name = request.form['target_user']

    user = user.query.filter_by(name=user_name).first()
    user.name=name
    user.email=email
    return render_template('index2.html')
    
myApp.run(debug=True)