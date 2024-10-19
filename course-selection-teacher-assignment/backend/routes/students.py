from flask import Blueprint, render_template
from backend.models.student import Student

students_bp = Blueprint('students', __name__)

@students_bp.route('/students')
def list_students():
    students = Student.query.all()
    return render_template('students.html', students=students)
