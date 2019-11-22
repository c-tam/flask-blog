from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/about")
def about():
    return render_template("about.html")

@main.route("/pinned")
def pinned():
    return render_template("pinned.html")

@main.route("/test")
def test():
    tags = request.args.get("tags")
    return str(tags)

