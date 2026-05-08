#!/usr/bin/python3
"""
API Security and Authentication using Flask-HTTPAuth and Flask-JWT-Extended.
Provides basic auth, JWT auth, and role-based access control.
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, get_jwt,
    get_jwt_identity, jwt_required
)
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

# JWT konfiqurasiyası üçün gizli açar təyin edirik
app.config["JWT_SECRET_KEY"] = "super-secret-key-change-in-production"
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# İstifadəçi verilənləri bazası
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# --- Basic Authentication İdarə Edilməsi ---

@auth.verify_password
def verify_password(username, password):
    """Verifies the username and password for Basic Authentication."""
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


@auth.error_handler
def basic_auth_error(status):
    """Returns a consistent 401 Unauthorized error for Basic Auth failures."""
    return jsonify({"error": "Unauthorized"}), 401


# --- Custom JWT Xəta İdarəediciləri (Testlərdən keçmək üçün önəmlidir) ---

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Triggered when no JWT is provided."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Triggered when an invalid JWT is provided."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err, expired_data):
    """Triggered when an expired JWT is provided."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err, revoked_data):
    """Triggered when a revoked JWT is provided."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Triggered when a fresh token is required but not provided."""
    return jsonify({"error": "Fresh token required"}), 401


# --- Endpoint-lər (Marşrutlar) ---

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Route protected by HTTP Basic Authentication."""
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """
    Logs in a user and returns a JWT token.
    Expects a JSON body with username and password.
    """
    json_data = request.get_json(silent=True)
    if not json_data:
        return jsonify({"error": "Missing JSON in request"}), 400

    username = json_data.get("username")
    password = json_data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Rol məlumatını JWT-nin içərisinə (claims) əlavə edirik
    additional_claims = {"role": user["role"]}
    access_token = create_access_token(
        identity=username,
        additional_claims=additional_claims
    )
    return jsonify(access_token=access_token)


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Route protected by JWT Authentication."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Route protected by JWT with Role-based access control (Admin only)."""
    # Token-in içərisindəki əlavə məlumatları (claims) alırıq
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
