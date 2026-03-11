from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my Flask API!👏👏👏"

@app.route('/student1')
def get_student():
    return jsonify({
        "name": "Mark Louie",
        "Year": 3,
        "Course": "BSIT"
})
@app.route('/student2')
def get_student1():
    return jsonify({
        "name": "Hiren Joy",
        "Year": 2,
        "Course": "BSN"
})
@app.route('/student3')
def get_student2():
    return jsonify({
        "name": "Jermilyn",
        "Year": 3,
        "Course": "BSIT"
})
@app.route('/student4')
def get_student3():
    return jsonify({
        "name": "Rene Rose",
        "Year": 3,
        "Course": "BSIT"
})
@app.route('/student5')
def get_student4():
    return jsonify({
        "name": "Mae Lou",
        "Year": 3,
        "Course": "BSIT"
})
@app.route('/student6')
def get_student5():
    return jsonify({
        "name": "Benjamin",
        "Year": 3,
        "Course": "BSIT"
})
