from db import db
from flask import session
from sqlalchemy.sql import text

def add_item(type, model, condition):
    sql = text("INSERT INTO library (type, model, condition) VALUES (:type,:model,:condition)")
    db.session.execute(sql, {"type":type, "model":model, "condition":condition})
    db.session.commit()
