from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

students = [
    {"name": "Mark Louie", "Year": 3, "Course": "BSIT", "Grade": 92},
    {"name": "Hiren Joy", "Year": 2, "Course": "BSN", "Grade": 88},
    {"name": "Jermilyn", "Year": 3, "Course": "BSIT", "Grade": 90},
    {"name": "Rene Rose", "Year": 3, "Course": "BSIT", "Grade": 91},
    {"name": "Mae Lou", "Year": 3, "Course": "BSIT", "Grade": 89},
    {"name": "Benjamin", "Year": 3, "Course": "BSIT", "Grade": 87}
]

@app.route('/')
def home():
    return "Welcome to my Flask API!👏👏👏"


@app.route('/student1')
def get_student():
    return jsonify(students[0])

@app.route('/student2')
def get_student1():
    return jsonify(students[1])

@app.route('/student3')
def get_student2():
    return jsonify(students[2])

@app.route('/student4')
def get_student3():
    return jsonify(students[3])

@app.route('/student5')
def get_student4():
    return jsonify(students[4])

@app.route('/student6')
def get_student5():
    return jsonify(students[5])


# SEARCH PAGE UI
@app.route('/search')
def search_page():

    html = """
    <!DOCTYPE html>
    <html>
    <head>
    <title>Student Search</title>

    <style>
    body{
        font-family:Arial;
        background:linear-gradient(135deg,#4facfe,#00f2fe);
        text-align:center;
        padding:50px;
    }

    .box{
        background:white;
        padding:40px;
        border-radius:10px;
        width:400px;
        margin:auto;
        box-shadow:0 0 15px rgba(0,0,0,0.2);
    }

    input{
        padding:10px;
        width:70%;
        border-radius:5px;
        border:1px solid #ccc;
    }

    button{
        padding:10px 20px;
        background:#007BFF;
        color:white;
        border:none;
        border-radius:5px;
        cursor:pointer;
    }

    button:hover{
        background:#0056b3;
    }

    #result{
        margin-top:20px;
        font-size:18px;
    }
    </style>

    </head>

    <body>

    <div class="box">
        <h2>Search Student</h2>

        <input type="text" id="name" placeholder="Enter student name">
        <button onclick="searchStudent()">Search</button>

        <div id="result"></div>
    </div>

    <script>

    function searchStudent(){

        let name = document.getElementById("name").value;

        fetch("/api/search?name=" + name)
        .then(res => res.json())
        .then(data => {

            if(data.error){
                document.getElementById("result").innerHTML = "Student not found";
            }
            else{
                document.getElementById("result").innerHTML =
                "<b>Name:</b> " + data.name +
                "<br><b>Year:</b> " + data.Year +
                "<br><b>Course:</b> " + data.Course +
                "<br><b>Grade:</b> " + data.Grade;
            }

        });

    }

    </script>

    </body>
    </html>
    """

    return render_template_string(html)


# SEARCH API
@app.route('/api/search')
def search_student():

    name = request.args.get("name")

    for s in students:
        if name.lower() in s["name"].lower():
            return jsonify(s)

    return jsonify({"error":"Student not found"})


if __name__ == '__main__':
    app.run(debug=True)
