from flask_login import UserMixin
from . import db

tagged_posts = db.Table("tagged_posts", 
    db.Column("post_id", db.Integer, db.ForeignKey("blog_post.id")),
    db.Column("tag_id", db.Integer, db.ForeignKey("blog_tag.id"))
)

class blog_post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    title_ = db.Column(db.String(50), unique=True)
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)
    tags = db.relationship("blog_tag", secondary=tagged_posts, backref=db.backref("posts", lazy="dynamic"))

class blog_tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(50))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
