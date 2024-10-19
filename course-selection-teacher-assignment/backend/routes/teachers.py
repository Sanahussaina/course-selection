from flask import Blueprint, jsonify
from backend.models.teacher import Teacher
from backend.database.db import db

teachers_bp = Blueprint('teachers', __name__)

@teachers_bp.route('/<int:course_id>', methods=['GET'])
def get_teachers(course_id):
    # Assuming each course has a list of teachers related to it
    teachers = Teacher.query.filter(Teacher.courses.any(id=course_id)).all()
    return jsonify([{'id': t.id, 'name': t.name, 'rating': t.rating} for t in teachers])
