from datetime import datetime
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer,DateTime
from sqlalchemy.orm import sessionmaker
from models.models import User, engine,Project,individual,Review

DBSession = sessionmaker(bind=engine)
session = DBSession()
engine = create_engine('mysql+pymysql://root:Zyc123456789@csmysql.cs.cf.ac.uk:3306/c21122021_flask_cmt120')
Base = declarative_base()

def show_info_last():
    return session.query(User)[-1]

def create_project(name):
    project = Project(name=name)
    session.add(project)
    session.commit()
    session.refresh(project)


def read_projects():
    return session.query(Project).all()


def update_project(project_id, name):
    session.query(Project).filter_by(id=project_id).update({
        "name": name
    })
    session.commit()


def delete_project(project_id):
    session.query(Project).filter_by(id=project_id).delete()
    session.commit()

def update_individual(user_email,name,caddress,haddress,phone,sex,school):
    session.query(individual).filter_by(email=user_email).update({
        "name": name,
        'caddress':caddress,
        'haddress':haddress,
        'phone':phone,
        'sex':sex,
        'school':school
    })
    session.commit()

def create_talk(content,user_email):
    review = Review(content=content,email=user_email)
    session.add(review)
    session.commit()
    session.refresh(review)


def read_talk():
    return session.query(Review).all()[-3:]

def read_one_talk(user_email):
    return session.query(Review).filter_by(email=user_email).all()

def delete_talk(id):
    session.query(Review).filter_by(id=id).delete()
    session.commit()