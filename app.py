from flask import Flask, request, jsonify
import json

app = Flask(__name__)

API_KEY = "12345"

students = [
    {"id": 1, "name": "John", "marks": 85},
    {"id": 2, "name": "Alice", "marks": 90}
]


def authenticate():
    return request.headers.get("X-API-Key") == API_KEY


@app.route("/")
def home():
    return jsonify({"message": "Flask REST API is running"})


@app.route("/students", methods=["GET"])
def get_students():
    if not authenticate():
        return jsonify({"error": "Unauthorized"}), 401

    return app.response_class(
        json.dumps(students, indent=4),
        mimetype="application/json"
    )


@app.route("/students", methods=["POST"])
def add_student():
    if not authenticate():
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()

    student = {
        "id": len(students) + 1,
        "name": data["name"],
        "marks": data["marks"]
    }

    students.append(student)

    return jsonify(student), 201


@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    if not authenticate():
        return jsonify({"error": "Unauthorized"}), 401

    global students
    students = [s for s in students if s["id"] != id]

    return jsonify({"message": "Student deleted"})


if __name__ == "__main__":
    app.run(debug=True)