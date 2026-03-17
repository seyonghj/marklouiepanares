from flask import Flask, jsonify, request, render_template_string
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# DATABASE (temporary list)
students = [
    {"id": 1, "name": "Mark Louie", "year": 3, "course": "BSIT", "grade": 92},
    {"id": 2, "name": "Hiren Joy", "year": 2, "course": "BSN", "grade": 88},
    {"id": 3, "name": "Jermilyn", "year": 3, "course": "BSIT", "grade": 90},
]

# HOME
@app.route('/')
def home():
    return "API is running 🚀"

# ✅ GET ALL STUDENTS (THIS FIXES YOUR UI)
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# ✅ ADD STUDENT (FOR YOUR UI FORM)
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()

    if not data or 'name' not in data:
        return jsonify({"error": "Name is required"}), 400

    new_student = {
        "id": len(students) + 1,
        "name": data["name"],
        "year": data.get("year", 1),
        "course": data.get("course", "N/A"),
        "grade": data.get("grade", 0)
    }

    students.append(new_student)
    return jsonify(new_student), 201

# OPTIONAL: GET ONE STUDENT
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = next((s for s in students if s["id"] == id), None)

    if not student:
        return jsonify({"error": "Not found"}), 404

    return jsonify(student)

# SEARCH API
@app.route('/api/search')
def search_student():
    name = request.args.get("name")

    for s in students:
        if name.lower() in s["name"].lower():
            return jsonify(s)

    return jsonify({"error": "Student not found"})

# SEARCH PAGE UI (unchanged)
@app.route('/search')
def search_page():
    return render_template_string(\"\"\" 
    <!-- your existing HTML here (no changes needed) -->
    \"\"\")

# ✅ RENDER FIX (IMPORTANT)
if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
