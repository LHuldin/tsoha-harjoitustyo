from db import db
from flask import session
from sqlalchemy.sql import text
from flask_sqlalchemy import SQLAlchemy

def add_item(type, model, condition):
    try:
        sql = text("INSERT INTO library (type, model, condition) VALUES (:type,:model,:condition)")
        db.session.execute(sql, {"type":type, "model":model, "condition":condition})
        db.session.commit()
    except:
        return False
    return True

def items():
    result = db.session.execute(text("SELECT type, model FROM library"))
    items = result.fetchall()
    return items

def add_software(name, mediatype, model, condition, value):
    try:
        sql = text("INSERT INTO software (name, mediatype, model, condition, value) VALUES (:name,:mediatype,:model,:condition,:value)")
        db.session.execute(sql, {"name":name, "type":mediatype, "model":model, "condition":condition, "value":value})
        db.session.commit()
    except:
        return False
    return True

def add_hardware(type, model, condition, value):
    try:
        sql = text("INSERT INTO hardware (type, model, condition, value) VALUES (:type,:model,:condition,:value)")
        db.session.execute(sql, {"type":type, "model":model, "condition":condition, "value":value})
        db.session.commit()
    except:
        return False
    return True