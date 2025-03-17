from flask import Blueprint, request, jsonify
from app import db
from app.models import Task

todo_bp = Blueprint('todo_bp', __name__)
@todo_bp.route('/')
def home():
    return jsonify({"message":"welcome to flask app"})
@todo_bp.route('/favicon.ico')
def favicon():
    return "", 204  # Empty response with 204 No Content

# Create a new task
@todo_bp.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    new_task = Task(title=data['title'], description=data.get('description', ''))
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Task added!", "task": new_task.to_dict()}), 201

# Get all tasks
@todo_bp.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])

# Update a task
@todo_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.json
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.completed = data.get('completed', task.completed)
    db.session.commit()
    return jsonify({"message": "Task updated!", "task": task.to_dict()})

# Delete a task
@todo_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted!"})

