from db import db
from flask import session
from sqlalchemy.sql import text
from flask_sqlalchemy import SQLAlchemy
import users

#def add_item(type, model, condition):
#    user_id = users.user_id()
#    if user_id == 0:
#        return False
#    
#    try:
#        sql = text("INSERT INTO library (type, model, condition) VALUES (:type,:model,:condition)")
#        db.session.execute(sql, {"type":type, "model":model, "condition":condition})
#        db.session.commit()
#    except:
#        return False
#    return True

def items():
    result = db.session.execute(text("SELECT * FROM software"))
    items = result.fetchall()
    return items

def switems():
    user_id = users.user_id()
    result = db.session.execute(text("SELECT * FROM software WHERE user_id = :user_id AND visible = true"), {"user_id":user_id})
    items = result.fetchall()
    return items

def hwitems():
    user_id = users.user_id()
    result = db.session.execute(text("SELECT * FROM hardware WHERE user_id = :user_id AND visible = true"), {"user_id":user_id})
    items = result.fetchall()
    return items

def public_switems():
    result = db.session.execute(text("SELECT * FROM software WHERE public = true AND visible = true"))
    items = result.fetchall()
    return items

def public_hwitems():
    result = db.session.execute(text("SELECT * FROM hardware WHERE public = true AND visible = true"))
    items = result.fetchall()
    return items

def swvalue():
    user_id = users.user_id()
    result = db.session.execute(text("SELECT sum(S.value) FROM software S WHERE S.user_id = :user_id AND visible = true"), {"user_id":user_id})
    sum_value = result.fetchone()[0]
    return sum_value

def hwvalue():
    user_id = users.user_id()
    result = db.session.execute(text("SELECT sum(H.value) FROM hardware H WHERE H.user_id = :user_id AND visible = true"), {"user_id":user_id})
    sum_value = result.fetchone()[0]
    return sum_value


def add_software(name, mediatype, model, condition, value, public, visible):
    user_id = users.user_id()
    if user_id == 0:
        return False
    try:
        sql = text("INSERT INTO software (user_id, name, mediatype, model, condition, value, public, visible) VALUES (:user_id,:name,:mediatype,:model,:condition,:value,:public,:visible)")
        db.session.execute(sql, {"user_id":user_id, "name":name, "mediatype":mediatype, "model":model, "condition":condition, "value":value, "public":public, "visible":visible})
        db.session.commit()
    except:
        return False
    return True

def add_hardware(type, model, condition, value, public, visible):
    user_id = users.user_id()
    if user_id == 0:
        return False                                                                                           
    try:
        sql = text("INSERT INTO hardware (user_id, type, model, condition, value, public, visible) VALUES (:user_id,:type,:model,:condition,:value,:public,:visible)")
        db.session.execute(sql, {"user_id":user_id, "type":type, "model":model, "condition":condition, "value":value, "public":public, "visible":visible})
        db.session.commit()
    except:
        return False
    return True

def drop_item(itemtype, id):
    if itemtype == "hw":
        try:
            result = db.session.execute(text("UPDATE hardware SET visible=false WHERE id = :id"), {"id":id})
            db.session.commit()
        except:
            return False
        return True
    elif itemtype == "sw":
        try:
            result = db.session.execute(text("UPDATE software SET visible=false WHERE id = :id"), {"id":id})
            db.session.commit()
        except:
            return False
        return True