from flask import render_template, redirect, url_for, jsonify
from flask import request
from flask import make_response
from sqlalchemy import or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import and_

from models.models import User, engine,Project,individual,Review
from . import index_blu
from . import handle

@index_blu.route("/profile/<email>",methods=["GET", "POST"])
def profile(email):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()


    obj = session.query(individual).filter(or_(email == individual.email)).first()

    session.close()
    if request.method=='GET':
        return render_template("index/profile.html", obj = obj,user_email=email)
    elif request.method=='POST':
        se = request.form['se']
        eb = request.form['eb']
        sex = request.form['sex']
        ot = request.form['ot']

        return render_template("index/profile.html", obj=obj,user_email=email,se=se,eb=eb,sex=sex,ot=ot)




@index_blu.route("/")
def view():
    return render_template('index/initial_page.html')

@index_blu.route("/login",methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form.get("Email")
        passwd = request.form.get("Password")
        if not email or not passwd:
            return render_template('index/inform.html')

        response = make_response("email:%s ，passwd:%s" % (email, passwd))

        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        try:
            obj = session.query(User).filter(and_(User.email == email, User.passwd == passwd, )).one()
        except:
            response.set_cookie("login_flag", "fail")
            return render_template('index/fail.html')
        else:
            response.set_cookie("login_flag", "success")
            print('success')
            return render_template("index/first_view.html", user_name=obj.user_name,user_email=obj.email)
    else:
        return render_template("index/login.html")


@index_blu.route("/logout")
def logout():
    response = make_response(redirect(url_for("index.login")))
    response.delete_cookie("login_flag")
    response.delete_cookie("user_id")
    return response


@index_blu.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("Email")
        user_name = request.form.get("Name")
        password = request.form.get("Password")


        if not (email and user_name and password):
            ret = {
                'email':email,
                'user_name': user_name,
                'password':password,
                "status": 2,
                "errmsg": "error"
            }
            return render_template('index/register.html')

        db_session = sessionmaker(bind=engine)()
        user_ret = db_session.query(User).filter(or_(User.email == email, User.user_name == user_name)).first()
        if user_ret:
            ret = {
                "status": 1,
                "errmsg": "email exists"
            }
            return render_template('index/register_info.html')
        else:

            new_user = User(email=email, passwd=password, user_name=user_name)
            db_session.add(new_user)
            db_session.commit()

            ret = {
                "status": 0,
                "errmsg": "success"
            }
            db_session.close()
            return render_template("index/register_success.html", user_name=user_name)


    elif request.method == "GET":
        return render_template("index/register.html")


@index_blu.route("/fail")
def fail_login():
    return render_template('index/fail.html')


@index_blu.route('/first_view/<user_email>')
def view_index(user_email):
    other_judges = handle.read_talk()
    return render_template('index/first_view.html',user_email=user_email,other_judges=other_judges)


@index_blu.route("/about_me/<user_email>", methods=["POST", "GET"])
def about_me_project(user_email):
    if request.method=='GET':
        return render_template('index/about_me.html',user_email=user_email)
    elif request.method=='POST':
        name = request.form.get("name") if request.form.get("name") else ''
        caddress = request.form.get("Caddress") if request.form.get("Caddress") else ''
        haddress = request.form.get("Haddress") if request.form.get("Haddress") else ''
        phone = request.form.get('phone') if request.form.get('phone') else ''
        sex = 'male' if request.form.get('gender') == 0 else 'Female'
        school = request.form.get('school') if request.form.get('school') else ''

        db_session = sessionmaker(bind=engine)()
        user_ret = db_session.query(individual).filter(or_(individual.email == user_email)).first()
        if user_ret:
            handle.update_individual(user_email,name,caddress,haddress,phone,sex,school)
        else:
            new_user = individual(email=user_email,name=name,caddress=caddress,haddress=haddress,phone=phone,sex=sex,school=school)
            db_session.add(new_user)
        db_session.commit()

        return render_template('index/about_me.html',user_email=user_email,name=name,caddress=caddress,haddress=haddress,sex=sex,phone=phone,school=school)

@index_blu.route("/review/<user_email>", methods=["POST", "GET"])
def review(user_email):
    if request.method=='POST':
        if request.form['content']:
            handle.create_talk(request.form['content'],user_email)
    return render_template('index/review.html',user_email=user_email,my_judge = handle.read_one_talk(user_email))


@index_blu.route("/review/<user_email>/<id>", methods=["POST", "GET"])
def review2(user_email,id):
    handle.delete_talk(id)
    return redirect(f'/review/{user_email}',code=302)