from backend.database.db import db

class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    year_of_study = db.Column(db.Integer, nullable=False)
    department = db.Column(db.String(100), nullable=False)

    feedbacks = db.relationship('Feedback', backref='student', lazy=True)

    def __repr__(self):
        return f'<Student {self.name}>'
