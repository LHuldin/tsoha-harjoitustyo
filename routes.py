from app import app
from flask import render_template, redirect, request
from db import db
from sqlalchemy.sql import text
import users, collection


@app.route("/")
def index():
    db.session.execute(text("INSERT INTO visitors (time) VALUES (NOW())"))
    db.session.commit()
    result = db.session.execute(text("SELECT COUNT(*) FROM visitors"))
    counter = result.fetchone()[0]
    result2 = db.session.execute(text("SELECT COUNT(*) FROM users"))
    rusers = result2.fetchone()[0]
    return render_template("index.html", counter=counter, rusers=rusers)

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
    hw_list = collection.hwitems()
    sw_list = collection.switems()
    swvalue = collection.swvalue()
    if swvalue is None:
        swvalue = 0
    hwvalue = collection.hwvalue()
    if hwvalue is None:
        hwvalue = 0
    sum = swvalue + hwvalue
    return render_template("mypage.html", swsum=swvalue, hwsum=hwvalue, sum=sum, hw_list=hw_list, sw_list=sw_list)

#@app.route("/additem",  methods=["GET", "POST"])
#def additem():
#    if request.method == "GET":
#        return render_template("additem.html")
#    if request.method == "POST":
#        type = request.form["type"]
#        model = request.form["model"]
#        condition = request.form["condition"]
#        if len(type) < 1 or len(model) < 1 or len(condition) < 1:
#            return render_template("error.html", message="Lisäys ei onnistunut")
#        if collection.add_item(type, model, condition):
#            return redirect("/mypage")
#        return render_template("error.html", message="Lisäys ei onnistunut")


    #return render_template("additem.html")

@app.route("/addhardware",  methods=["GET", "POST"])
def addhardware():
    if request.method == "GET":
        return render_template("addhardware.html")
    if request.method == "POST":
        type = request.form["type"]
        model = request.form["model"]
        condition = request.form["condition"]
        value = request.form["value"]
        public = request.form["public"]
        visible = "true"
        if len(type) < 1 or len(model) < 1 or len(condition) < 1:
            return render_template("error.html", message="Lisäys ei onnistunuttest")
        if collection.add_hardware(type, model, condition, value, public, visible):
            return redirect("/mypage")
        return render_template("error.html", message="Lisäys ei onnistunuttoast")
    
@app.route("/addsoftware",  methods=["GET", "POST"])
def addsoftware():
    if request.method == "GET":
        return render_template("addsoftware.html")
    if request.method == "POST":
        name = request.form["name"]
        type = request.form["mediatype"]
        model = request.form["model"]
        condition = request.form["condition"]
        value = request.form["value"]
        public = request.form["public"]
        visible = "true"
        if len(type) < 1 or len(model) < 1 or len(condition) < 1:
            return render_template("error.html", message="Lisäys ei onnistunut")
        if collection.add_software(name,  type, model, condition, value, public, visible):
            return redirect("/mypage")
        return render_template("error.html", message="Lisäys ei onnistunut")



@app.route("/items")
def items():
    items_list = collection.items()
    return render_template("items.html", count=len(items_list), items_list = items_list)

@app.route("/publicpage")
def publicpage():
    hw_list = collection.public_hwitems()
    sw_list = collection.public_switems()
    return render_template("publicpage.html", hw_list = hw_list, sw_list = sw_list)


@app.route("/dropitem",  methods=["GET", "POST"])
def dropitem():
    if request.method == "GET":
        hw_list = collection.hwitems()
        sw_list = collection.switems()
        return render_template("dropitem.html", hw_list=hw_list, sw_list=sw_list)
    if request.method == "POST":
        itemtype = request.form["itemtype"]
        id = request.form["id"]
        if collection.drop_item(itemtype, id):
            return redirect("/mypage")
        return render_template("error.html", message="Poisto ei onnistunut")

