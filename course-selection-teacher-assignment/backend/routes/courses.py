from flask import Blueprint, jsonify
from backend.models.course import Course
from backend.database.db import db

courses_bp = Blueprint('courses', __name__)

@courses_bp.route('/', methods=['GET'])
def get_courses():
    theory_courses = Course.query.filter_by(course_type='Theory').all()
    lab_courses = Course.query.filter_by(course_type='Lab').all()
    return jsonify({
        'theory_courses': [{'id': c.id, 'name': c.name} for c in theory_courses],
        'lab_courses': [{'id': c.id, 'name': c.name} for c in lab_courses]
    })
