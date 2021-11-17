from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    blogs = db.relationship('Blog', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')
    upvote = db.relationship("Upvote",backref="user",lazy="dynamic")
    downvote = db.relationship("Downvote",backref="user",lazy="dynamic")
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'
    
class Blog(db.Model):
    __tablename__ = "blogs"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    post = db.Column(db.Text())
    time = db.Column(db.DateTime, default = datetime.utcnow)
    category = db.Column(db.String(255), index = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comment = db.relationship('Comment', backref='blog', lazy='dynamic')
    upvote = db.relationship("Upvote",backref="blog",lazy="dynamic")
    downvote = db.relationship("Downvote",backref="blog",lazy="dynamic")
        
    def save_blog(self):
        db.session.add(self)
        db.session.commit()

        
    def __repr__(self):
        return f'Blog {self.post}'
    
class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text())
    blog_id = db.Column(db.Integer,db.ForeignKey("blogs.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,blog_id):
        comments = Comment.query.filter_by(blog_id=blog_id).all()

        return comments

    
    def __repr__(self):
        return f'comment:{self.comment}'
    
class Upvote(db.Model):
    __tablename__ = "upvotes"

    id = db.Column(db.Integer,primary_key=True)
    blog_id = db.Column(db.Integer,db.ForeignKey("blogs.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_upvotes(cls,id):
        upvote = Upvote.query.filter_by(blog_id=id).all()
        return upvote


    def __repr__(self):
        return f'{self.user_id}:{self.blog_id}'

class Downvote(db.Model):
    __tablename__ = "downvotes"

    id = db.Column(db.Integer,primary_key=True)
    blog_id = db.Column(db.Integer,db.ForeignKey("blogs.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
   
    def save(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_downvotes(cls,id):
        downvote = Downvote.query.filter_by(blog_id=id).all()
        return downvote

    def __repr__(self):
        return f'{self.user_id}:{self.blog_id}'