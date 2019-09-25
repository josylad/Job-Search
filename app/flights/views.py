import os
from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint, current_app)
from flask_login import current_user, login_required, logout_user
from app import db, bcrypt
import secrets
from PIL import Image
from app.request import get_quote
from app.models import Post, User, Comment
from app.posts.forms import PostForm, CommentForm
from app.request import get_quote
from flask_simplemde import SimpleMDE
from ..main import views


posts = Blueprint('posts', __name__)
quotes = get_quote()


def save_picture(form_image):
    randome_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(form_image.filename)
    picture_name = randome_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/featured_images', picture_name)
    
    output_size = (1000, 400)
    final_image = Image.open(form_image)
    final_image.thumbnail(output_size)
    
    final_image.save(picture_path)
    
    return picture_name


@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    
    if form.validate_on_submit():
        pic =None
        if form.image.data:
            picture_file = save_picture(form.image.data)
            final_pic = picture_file
            pic= final_pic
        post = Post(title=form.title.data, content=form.content.data, author=current_user, category=form.category.data, image=pic)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been published!', 'success')
        return redirect(url_for('main.home'))
    
    myposts = Post.query.order_by(Post.posted_date.desc())
    return render_template('new-post.html', title='New Post', form=form, legend='New Post', myposts=myposts, quotes=quotes)


@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    comments = Comment.query.filter_by(post_id = post_id).all()
    myposts = Post.query.order_by(Post.posted_date.desc())
    return render_template('post.html', title=post.title, post=post, comments = comments, myposts=myposts, quotes=quotes)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        if form.image.data:
            picture_file = save_picture(form.image.data)
            final_pic = picture_file
             
             
        post.title = form.title.data
        post.content = form.content.data
        post.category = form.category.data
        post.image = final_pic
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        form.category.data = post.category
    myposts = Post.query.order_by(Post.posted_date.desc())
    return render_template('new-post.html', title='Update Post', form=form, legend='Update Post', quotes=quotes, myposts=myposts)


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))


@posts.route("/post/<string:category>")
def category_post(category):
    post = Post.query.filter_by(category=category).all()
    print("..............", post)
    myposts = Post.query.order_by(Post.posted_date.desc())
    return render_template('category.html', post=post, category=category, myposts=myposts, quotes=quotes) 


@posts.route("/post/<int:post_id>/comment", methods=['GET', 'POST'])
@login_required
def new_comment(post_id):
    post = Post.query.get_or_404(post_id)
    
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(comment=form.comment.data, fullname=form.name.data, author=current_user, post_id = post_id )
        db.session.add(comment)
        db.session.commit()
        # comments = Comment.query.all()
        flash('You comment has been created!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    myposts = Post.query.order_by(Post.posted_date.desc())
    return render_template('new-comment.html', title='New Comment', form=form, legend='New Comment', myposts=myposts, quotes=quotes)


@posts.route('/deleteComment/<int:comment_id>/<int:post_id>', methods=["GET", "POST"])
def deleteComment(comment_id, post_id):
    post = Post.query.get_or_404(post_id)
    
    comment = Comment.query.filter_by(id=comment_id).first()
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for("posts.post", post_id=post.id))


@posts.route("/comment/<int:id>")
def commentpage(id):
    comments = Comment.query.filter_by(id = id).all()
    return render_template('comment.html', title=Comment, comments = comments)



@posts.route("/comment/<int:comment_id>/delete", methods=['POST'])
@login_required
def comment(coment_id):
    post = Post.query.get_or_404(post_id)
    comments = Comment.query.get_or_404(comment_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(comments)
    db.session.commit()
    flash('The comment has been deleted!', 'success')
    return redirect(url_for('posts.post', comment_id=comment.id))


@posts.route('/quote')
def getquotes():

    quotes = get_quote()
    # title = name
    
    return render_template('layout.html', quotes=quotes)