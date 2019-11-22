from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from . import db

auth = Blueprint("auth", __name__)

@auth.route("/blog/login")
def login():
    return render_template("login.html")

@auth.route("/blog/login", methods=["POST"])
def login_post():
    username = request.form.get("user")
    password = request.form.get("password")
    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        flash("Invalid credentials")
        return redirect(url_for("auth.login"))
    login_user(user)

    return redirect(url_for("blog.posts"))

@auth.route("/blog/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("blog.posts"))

@auth.route("/blog/newuser")
def newuser():
    return render_template("newuser.html")

@auth.route("/blog/newuser", methods=["POST"])
def newuser_post():
    username = request.form.get("user")
    password = request.form.get("password")
    user = User.query.filter_by(username=username).first()
    if not username or not password:
        flash("Fill all fields")
        return redirect(url_for("auth.newuser"))
    elif user:
        flash("Username already exists")
        return redirect(url_for("auth.newuser"))
    new_user = User(username=username, password=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()
    flash("Made new user")
    return redirect(url_for("auth.newuser"))

@auth.route("/blog/edituser")
@login_required
def edituser():
    users = User.query.all()

    return render_template("edituser.html", users=users)

@auth.route("/blog/edituser", methods=["POST"])
@login_required
def edituser_post():
    id = request.get_json()["id"]
    password = request.get_json()["password"]
    user = User.query.filter_by(id=id).first()
    user.password = generate_password_hash(password)
    db.session.commit()
    
    return jsonify({"message": "Changed user  #{}'s password".format(id)})

@auth.route("/_deleteuser", methods=["POST"])
@login_required
def delete_user():
    id = request.get_json()["id"]
    print(id)
    print(type(id))
    print(int(id))
    print(int(id)==1)
    if int(id) == 1:
        return jsonify({"message": "Cannot delete user #1"})
    else:
        user = User.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "Deleted user #{}".format(id)})
