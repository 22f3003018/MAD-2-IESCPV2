from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String,unique=True,nullable=False)
    password = db.Column(db.String,nullable=False)
    # flask-security 
    fs_specifier=db.Column(db.String,unique=True,nullable=False)
    active = db.Column(db.Boolean,default=True)
    roles = db.Relationship('Role',backref='bearers',secondary='user_roles')

class Role(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,unique=True,nullable=False)
    description = db.Column(db.String,nullable=True)

class UserRole(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id= db.Column(db.Integer,db.ForeignKey('user.id'))
    role_id= db.Column(db.Integer,db.ForeignKey('role.id'))
