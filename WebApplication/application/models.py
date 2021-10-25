from flask_sqlalchemy import SQLAlchemy
from application import db
from datetime import datetime

class Tasks(db.Model):

    __tablename__ = "Tasks"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('Task.id', ondelete='CASCADE'))
    task_title = db.Column(db.String(30), nullable=True)
    deadline = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    module = db.Column(db.String(20), nullable=True)
    desc = db.Column(db.String(50), nullable=True)
    complete = db.Column(db.Boolean)