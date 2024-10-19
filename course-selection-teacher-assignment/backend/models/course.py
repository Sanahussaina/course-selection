from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    academic_background = db.Column(db.String(255))
    rating = db.Column(db.Float)
    courses = db.relationship('Course', secondary='course_teachers', back_populates='teachers')

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    course_type = db.Column(db.String(50))  # Theory or Lab
    teachers = db.relationship('Teacher', secondary='course_teachers', back_populates='courses')

class CourseTeachers(db.Model):
    __tablename__ = 'course_teachers'
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), primary_key=True)

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))
    student_feedback = db.Column(db.Text)
