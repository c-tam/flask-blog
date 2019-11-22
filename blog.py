from flask import Flask, Blueprint, render_template, request, redirect, url_for, jsonify
from flask_login import login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from .models import blog_post, blog_tag
from . import db

blog = Blueprint("blog", __name__)

@blog.route("/blog/post/<title>")
def post_title(title):
    post = blog_post.query.filter_by(title_=title).one()
    return render_template("post.html", post=post) 

@blog.route("/blog")
def posts():
    page = request.args.get("page", 1, type=int)
    _tags = request.args.get("tags")
    _tag = blog_tag.query.filter_by(tag=_tags).first()
    if _tag is None:
        posts = blog_post.query.order_by(blog_post.date_posted.desc()).paginate(page=page, per_page=5, error_out=False)
    else:
        posts = _tag.posts.order_by(blog_post.date_posted.desc()).paginate(page=page, per_page=5, error_out=False)
    # next/prev urls
    next_url = url_for("blog.posts", page=posts.next_num) if posts.has_next else None
    prev_url = url_for("blog.posts", page=posts.prev_num) if posts.has_prev else None
    # tags
    tags = blog_tag.query.all()
    return render_template("blog.html", posts=posts, tags=tags, next_url=next_url, prev_url=prev_url, page=page, _tags=_tags) 

@blog.route("/blog/add")
@login_required
def add():
    return render_template("add.html")

@blog.route("/blog/add", methods=["POST"])
@login_required
def addpost():
    # get data
    data = request.get_json()
    title = data["title"]
    author = data["author"]
    content = data["content"]
    tags = data["tag"]
    # check if fields are full
    if (title and author and content and tags):
        
        # check for duplicate titles
        if db.session.query(blog_post.id).filter_by(title=title).scalar() is None:
            title_ = title.replace(" ", "-").replace("%", "-").lower()
            post = blog_post(title=title, title_=title_, author=author, date_posted=datetime.now(), content=content)
            db.session.add(post)
            db.session.commit()
            
            for i in tags:
                tag_id = db.session.query(blog_tag.id).filter_by(tag=i).scalar()
                # unique tags
                if tag_id is None:
                    tag = blog_tag(tag=i)
                    tag.posts.append(post)
                    db.session.commit()
                # duplicate tags
                else:
                    tag = blog_tag.query.filter_by(id=tag_id).scalar()
                    post.tags.append(tag)
                    db.session.commit() 
            
            return jsonify({'error': False, "message": "Success"})
        
        return jsonify({'error': True, "message": "Title already exists"})
    
    return jsonify({'error': True, "message": "Fill in all the fields"})

@blog.route("/_delete", methods=["POST"])
@login_required
def delete():
    id = request.get_json()["id"]
    post = blog_post.query.filter_by(id=id).first()
    db.session.delete(post)
    db.session.commit()
    return jsonify({"message": "Deleted post #{}".format(id)})
