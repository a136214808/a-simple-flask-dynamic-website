from flask import render_template
from sqlalchemy.orm import sessionmaker

from models.models import User, engine
from . import admin_blu


@admin_blu.route("/admin")
def index():
    return render_template("admin/admin.html")


@admin_blu.route("/user_info")
def user_info():
    DBSession = sessionmaker(bind=engine)  #
    session = DBSession()
    all_user_info = session.query(User).all()
    print(all_user_info)
    session.close()
    return render_template("admin/admin.html", user_infos=all_user_info)
