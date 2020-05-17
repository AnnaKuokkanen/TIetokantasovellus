from CourseEditor import app, db
from flask import render_template, request
from CourseEditor.users.models import User

@app.route("/users/new.html")
def tasks_form():
    return render_template("users/new.html")

@app.route("/users/", methods=["POST"])
def users_create():
    u = User(request.form.get("user"),
            request.form.get("pin"),
            request.form.get("fname"),
            request.form.get("lname"))

    db.session().add(u)
    db.session().commit()
  
    return "Kiitos!"