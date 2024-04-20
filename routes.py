from app import app
from flask import render_template, redirect, request
from db import db
from sqlalchemy.sql import text
import users


@app.route("/")
def index():
    db.session.execute(text("INSERT INTO visitors (time) VALUES (NOW())"))
    db.session.commit()
    result = db.session.execute(text("SELECT COUNT(*) FROM visitors"))
    counter = result.fetchone()[0]
    return render_template("index.html", counter=counter)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/mypage")
        else:
            return render_template("error.html", message="Kirjautuminen ei onnistunut")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if len(password) < 4:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")
        if users.register(username, password):
            return redirect("/mypage")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")
        
@app.route("/mypage")
def mypage():

    return render_template("mypage.html")

@app.route("/additem")
def additem():
    
    return render_template("additem.html")

@app.route("/items")
def items():
    
    return render_template("items.html")

@app.route("/dropitem")
def dropitem():
    
    return render_template("dropitem.html")