from flask import Blueprint, request, jsonify
from backend.models.feedback import Feedback
from backend.database.db import db

feedback_bp = Blueprint('feedback', __name__)

@feedback_bp.route('/submit', methods=['POST'])
def submit_feedback():
    data = request.json
    new_feedback = Feedback(
        student_id=data['student_id'],
        teacher_id=data['teacher_id'],
        feedback_text=data['feedback_text'],
        rating=data['rating']
    )
    db.session.add(new_feedback)
    db.session.commit()
    return jsonify({'message': 'Feedback submitted successfully!'})
