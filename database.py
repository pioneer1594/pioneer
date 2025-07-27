
from . import db,bcrypt
#one side must have relationship
#many side must have foreignkey

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True,autoincrement=True,nullable=False)
    Username = db.Column(db.String(100),nullable=False,unique=True)
    email=db.Column(db.String(100),nullable=False,unique=True)
    password=db.Column(db.String(100),nullable=False)
    CreateDate = db.Column(db.DateTime,nullable=False)
    #message=db.relationship(class name not table name ,backref=table_name,lazy is used to connect each table
    messages=db.relationship('Message',backref='user',lazy=True)


    #declare and assign new attribute
    #not equal to password In User(in the property passwords should not be equal to User.password)
    #in route.py,passwords is store form.password and in database.py,passwords property is to get
    #from User table.and hush
    #getter
    @property
    def passwords(self):
        return self.password

    #in the setter and getter methods, this name should be property's function-name
    #setter
    @passwords.setter
    def passwords(self, password_hash):
        self.password = bcrypt.generate_password_hash(password_hash).decode('utf-8')

class Message(db.Model):
    __tablename__ = 'message'
    message_id = db.Column(db.Integer, primary_key=True,autoincrement=True,nullable=False)
    content = db.Column(db.String(1000),nullable=False)
    result=db.Column(db.Boolean,nullable=False)
    reason=db.Column(db.String(1000),nullable=False)
    CreateDate = db.Column(db.DateTime,nullable=False)
    user_Id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)


class scam_analyzer(db.Model):
    __tablename__ = 'scamanalyzer'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True,nullable=False)
    Keywords=db.Column(db.String(100),nullable=False)
    CreateDate=db.Column(db.DateTime,nullable=False)

