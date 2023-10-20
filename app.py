from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database (a list of student dictionaries with dummy data)
students = [
    {"id": 1, "name": "Alice", "grade": "A"},
    {"id": 2, "name": "Bob", "grade": "B"},
    {"id": 3, "name": "Charlie", "grade": "C"},
]

# Create a new student
@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    student = {
        'id': data['id'],
        'name': data['name'],
        'grade': data['grade']
    }
    students.append(student)
    return jsonify(student), 201

# Read a student by ID
@app.route('/students/<int:student_id>', methods=['GET'])
def read_student(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if student is None:
        return jsonify({'error': 'Student not found'}), 404
    return jsonify(student)

# Update a student by ID
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    student = next((s for s in students if s['id'] == student_id), None)
    if student is None:
        return jsonify({'error': 'Student not found'}), 404
    student.update(data)
    return jsonify(student)

# Delete a student by ID
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if student is None:
        return jsonify({'error': 'Student not found'}), 404
    students.remove(student)
    return jsonify(student)

# Get a list of all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

if __name__ == '__main__':
    app.run(debug=True)
