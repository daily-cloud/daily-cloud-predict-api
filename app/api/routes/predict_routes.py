from flask import Blueprint, jsonify, request
from app import app
from app.api.utils.predict_text import predict_depression


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
        return jsonify({"message": "Predict Text API"}), 200
    elif request.method == "POST":
        try:
            request_data = request.form
            text = request_data["text"]

            # predicted_data = predict_depression(text)

            # depression = str(predicted_data["depression"])
            # confidence_score = str(predicted_data["confidence_score"])

            return (
                jsonify(
                    {
                        "status": "success",
                        "message": "Text predicted successfully!",
                        "data": {
                            "text": text,
                            # "depression": depression,
                            # "confidenceScore": confidence_score,
                        },
                    }
                ),
                200,
            )
        except Exception as e:
            return (
                jsonify(
                    {
                        "status": "error",
                        "message": "No text provided!, please provide text in the form of 'text'",
                        "error": str(e),
                    }
                ),
                500,
            )
