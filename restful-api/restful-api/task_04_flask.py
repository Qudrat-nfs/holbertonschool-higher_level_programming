#!/usr/bin/python3
"""
A simple REST API built using the Flask framework.
Provides endpoints to manage and retrieve user data.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# İstifadəçiləri yaddaşda saxlamaq üçün lüğət
users = {}


@app.route("/")
def home():
    """Returns a welcome message."""
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    """Returns the API status."""
    return "OK"


@app.route("/data")
def data():
    """Returns a list of all usernames stored in the API."""
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    """Returns the full object corresponding to the provided username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Parses incoming JSON data and adds a new user to the users dictionary."""
    # 1. Göndərilən məlumatın etibarlı JSON olub-olmadığını yoxlayırıq
    json_data = request.get_json(silent=True)
    if json_data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # 2. 'username' sahəsinin mövcudluğunu yoxlayırıq
    username = json_data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # 3. İstifadəçinin artıq mövcud olub-olmadığını yoxlayırıq
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # 4. İstifadəçini bazaya (lugətə) əlavə edirik və 201 qaytarırıq
    users[username] = json_data
    response_data = {
        "message": "User added",
        "user": json_data
    }
    return jsonify(response_data), 201


if __name__ == "__main__":
    app.run()
