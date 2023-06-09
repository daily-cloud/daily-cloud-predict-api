from flask import Blueprint, jsonify, request
from app import app

predict_image_routes = Blueprint("predict_image_routes", __name__)
predict_text_routes = Blueprint("predict_text_routes", __name__)

@predict_image_routes.route("/image", methods=["GET", "POST"])
def predict_image():
    if request.method == "GET":
        return jsonify({"message": "Predict Image!"}), 200
    elif request.method == "POST":
        return jsonify({"message": "Hello, World!"}), 200

@predict_text_routes.route("/text", methods=["GET", "POST"])
def predict_text():
    if request.method == "GET":
        return jsonify({"message": "Predict Text!"}), 200
    elif request.method == "POST":
        return jsonify({"message": "Hello, World!"}), 200
