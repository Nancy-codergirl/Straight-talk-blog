from flask import render_template,redirect,url_for,abort,flash,request
from app.main.forms import BlogForm
from . import main
from .. import db
from ..models import  User,Blog
from flask_login import login_required,current_user


#Views

#Deleting a blog view function
@main.route('/blog/<int:id>/delete', methods=['GET', 'POST'])
@login_required
def delete_blog(id):
    """
    Delete blog function that deletes the blog
    """
    blog = Blog.get_blog(id)

    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for('main.index', username=current_user.username))


#Updating blog view function
@main.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update_blog(id):
    blog = Blog.query.get_or_404(id)
    update_form = BlogForm()
    if update_form.validate_on_submit():
        blog.title = update_form.title.data
        blog.description = update_form.description.data
        db.session.add(blog)
        db.session.commit()

        return redirect(url_for('main.index'))
    elif request.method == 'GET':
        update_form.title.data = blog.title
        update_form.description.data = blog.description
    return render_template('update.html', blog=blog, update_form=update_form)