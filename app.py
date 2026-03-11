from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my Flask API!"

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