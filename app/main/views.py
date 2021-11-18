from flask import render_template,request,redirect,url_for,abort,flash

from app.email import mail_message
from . import main
from flask_login import login_required,current_user
from ..models import Upvote, User,Blog,Comment,Downvote
from .forms import UpdateProfile,BlogForm,CommentForm,UpdateBlog
from .. import db,photos


@main.route('/')
def index():
    blogs = Blog.query.order_by(Blog.time.desc()).all()
    general = Blog.query.filter_by(category = 'General').all()
    politics = Blog.query.filter_by(category = 'Politics').all()
    religion = Blog.query.filter_by(category = 'Religion').all()
    relationships = Blog.query.filter_by(category = 'Relationships').all()
    
    
    return render_template('index.html',blogs=blogs,general=general,politics=politics,religion=religion,relationships=relationships)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    profile_form = UpdateProfile()
    if profile_form.validate_on_submit():
        user.bio = profile_form.bio.data
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('.profile',uname=user.username))
    return render_template('profile/update.html',profile_form =profile_form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))



@main.route('/create_new',methods=['POST','GET'])
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data   
        category = form.category.data
        new_blog =Blog(title = title,post=post,user=current_user,category=category)
        new_blog.save_blog()
        return redirect(url_for('main.index'))
    
    return render_template('new_blog.html',form=form, title="Create Blog")

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



@main.route('/comment/<int:blog_id>',methods = ['POST','GET'])
@login_required
def comment(blog_id):
    form = CommentForm()
    blog = Blog.query.get(blog_id)
    comments = Comment.query.filter_by(blog_id=blog_id).all()
    if form.validate_on_submit():
        comment= form.comment.data
        new_comment= Comment(comment=comment,blog_id=blog_id)
        new_comment.save_comment()
        blog_id=blog_id
        return redirect(url_for('.comment',blog_id=blog_id))
    return render_template('comment.html',form=form,comments=comments,blog=blog)


@main.route('/read/<int:blog_id>')
def read(blog_id):
    blog = Blog.query.get(blog_id)
    return render_template('read.html',blog=blog)

@main.route("/update_post/<int:blog_id>",methods= ['POST','GET'])
@login_required
def update_post(blog_id):
    blog = Blog.query.get(blog_id)
    form = UpdateBlog()
    if form.validate_on_submit():
        blog.title =form.title.data
        blog.post = form.post.data
        db.session.commit()
        flash('Your post has been updated!',)
        return redirect(url_for('main.read',blog_id=blog_id))
    elif request.method == 'GET':
        form.title.data = blog.title
        form.post.data = blog.post
    return render_template('new_blog.html',form=form, titl='Update Blog')

@main.route("/delete_post/<int:blog_id>/delete",methods= ['POST'])
@login_required
def delete_post(blog_id):
    blog_delete = Blog.query.get(blog_id)
    db.session.delete(blog_delete)
    db.session.commit()
    flash('Your blog has been deleted!')
    return redirect(url_for('main.index'))

@main.route('/like/<int:id>',methods = ['POST','GET'])
@login_required
def upvote(id):
    blogs = Upvote.get_upvotes(id)
    user_id = f'{current_user.id}:{id}'
    for pitch in blogs:
        to_string = f'{pitch}'
        if user_id == to_string:
            return redirect(url_for('main.read',blog_id=id))
        else:
            continue
    new_vote = Upvote(user = current_user, blog_id=id)
    new_vote.save()
    return redirect(url_for('main.read',blog_id=id))

@main.route("/delete_comment/<int:blog_id>/<int:comment_id>",methods= ['POST'])
@login_required
def delete_comment(comment_id,blog_id):
    comment = Comment.query.filter_by(id=comment_id).first()
    db.session.delete(comment)
    db.session.commit()
    flash('Comment has been deleted!')
    return redirect(url_for('.comment', blog_id = blog_id))

@main.route('/blog/<int:id>', methods = ['GET','POST'])
def blog(id):
    blog = Blog.get_blog(id)
    posted_date = blog.time.strftime('%b %d, %Y')

    if request.args.get("like"):
        blog.likes = blog.likes + 1

        db.session.add(blog)
        db.session.commit()

        return redirect("/blog/{blog_id}".format(blog_id=blog.id))

    elif request.args.get("dislike"):
        blog.dislikes = blog.dislikes + 1

        db.session.add(blog)
        db.session.commit()

        return redirect("/blog/{blog_id}".format(blog_id=blog.id))
    
