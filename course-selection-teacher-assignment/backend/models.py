# models.py
from your_database_module import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    course_type = db.Column(db.String(50), nullable=False)  # 'Theory' or 'Lab'
