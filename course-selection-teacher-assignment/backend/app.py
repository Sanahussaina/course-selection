# app.py
from flask import Flask, jsonify
from .models import Course  # Ensure you're importing the Course model

app = Flask(__name__)

@app.route('/courses', methods=['GET'])
def get_courses():
    theory_courses = Course.query.filter_by(course_type='Theory').all()
    lab_courses = Course.query.filter_by(course_type='Lab').all()
    
    return jsonify({
        'theory_courses': [{'id': c.id, 'name': c.name} for c in theory_courses],
        'lab_courses': [{'id': c.id, 'name': c.name} for c in lab_courses]
    })
