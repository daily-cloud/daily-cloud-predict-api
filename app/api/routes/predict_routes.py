from flask import Blueprint, jsonify, request
from app import app
from app.api.utils.predict_depression import predict_depression


predict_depression_route = Blueprint("predict_depression_routes", __name__)


@predict_depression_route.route("/depression", methods=["GET", "POST"])
def predict_text():
    if request.method == "GET":
        return jsonify({"message": "Predict Depression API"}), 200
    elif request.method == "POST":
        try:
            request_data = request.form
            text = request_data["text"]

            if not text:
                raise Exception("No text provided!")

            predicted_data = predict_depression(text)

            depression = predicted_data["depression"]
            confidence_score = predicted_data["confidence_score"]

            return (
                jsonify(
                    {
                        "status": "success",
                        "message": "Text predicted successfully!",
                        "data": {
                            "text": text,
                            "depression": depression,
                            "confidenceScore": confidence_score,
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
                        "message": "No text provided!, please provide text string in the form of 'text'",
                        "error": str(e),
                    }
                ),
                500,
            )
