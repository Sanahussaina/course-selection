from backend.database.db import db

class Feedback(db.Model):
    __tablename__ = 'feedbacks'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<Feedback {self.id}>'
