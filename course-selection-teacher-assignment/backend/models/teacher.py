from backend.database.db import db

class Teacher(db.Model):
    __tablename__ = 'teachers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    academic_background = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    
    courses = db.relationship('Course', secondary='course_teacher', backref='teachers')

    def __repr__(self):
        return f'<Teacher {self.name}>'
