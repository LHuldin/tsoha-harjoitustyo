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