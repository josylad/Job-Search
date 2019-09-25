from datetime import datetime
from app import db, login_manager
from . import db
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(225), unique=True, nullable=False)
    fullname = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(255), unique= True, nullable= False, index = True)
    bio = db.Column(db.String(255))
    image = db.Column(db.String(225), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    facebook = db.Column(db.String())
    twitter = db.Column(db.String())
    github = db.Column(db.String())
    linkedin = db.Column(db.String())
    posts = db.relationship('Post', backref='author', lazy=True)
    comments = db.relationship('Comment', backref='author', lazy=True)

    
    def __repr__(self):
        return f'User {self.username}'
    

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    posted_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    content = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(225), default='default.jpg')
    category = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    comments = db.relationship('Comment', backref='post', lazy=True)

    
    def __repr__(self):
        return f"Post('{self.title}', '{self.posted_date}', '{self.category}')"
    

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(255))
    comment = db.Column(db.Text, nullable=False)
    posted_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comment(cls,id):
        comments = Comment.query.filter_by(post_id=id).all()
        return comments
    
    def __repr__(self):
        return f"Comment('{self.comment}', '{self.posted_date}')"
    
    
class Quote:
    '''
    Quote class to define Quote Objects
    '''

    def __init__(self, id, author, quote, permalink):
        self.id = id
        self.author = author
        self.quote = quote
        self.permalink = permalink