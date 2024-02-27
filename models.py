from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    projects = db.relationship('Project', backref='user', lazy=True)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    images = db.relationship('ImageData', backref='project', lazy=True)
    training_sessions = db.relationship('TrainingSession', backref='project', lazy=True)


class ImageData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_path = db.Column(db.String(200), nullable=False)
    labels = db.Column(db.String(200),
                       nullable=False)  # Simplified; consider a many-to-many relationship for a real project
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)


class TrainingSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end_time = db.Column(db.DateTime)
    status = db.Column(db.String(50), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    model_id = db.Column(db.Integer, db.ForeignKey('model.id'))


class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model_path = db.Column(db.String(200), nullable=False)
    performance_metrics = db.Column(db.String(500))  # JSON or structured string
    training_sessions = db.relationship('TrainingSession', backref='model', lazy=True)
