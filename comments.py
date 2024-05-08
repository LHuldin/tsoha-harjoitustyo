from db import db
from flask import session
from sqlalchemy.sql import text
from flask_sqlalchemy import SQLAlchemy
import users

def add_comment(comment):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = text("INSERT INTO comments (comment, user_id, t_stamp) VALUES (:comment, :user_id, NOW())")
    db.session.execute(sql, {"comment":comment, "user_id":user_id})
    db.session.commit()
    return True

def comments():
    sql = text("SELECT C.comment, U.username, C.t_stamp FROM comments C, users U WHERE C.user_id=U.id ORDER BY C.id DESC")
    result = db.session.execute(sql)
    return result.fetchall()