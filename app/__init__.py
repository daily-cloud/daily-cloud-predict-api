import nltk
from flask import Flask, request, jsonify

# from flask_cors import CORS

# Download NLTK data at first run
nltk.download("punkt")
nltk.download("stopwords")

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return (
            jsonify(
                {"message": "Welcome to Daily Cloud Predict API", "version": "0.1.2"}
            ),
            200,
        )
    elif request.method == "POST":
        return (
            jsonify({"message": "POST Success", "version": "0.1.2"}),
            200,
        )


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": "error", "message": "404 Resource Not Found"}), 404


from app.api.routes.predict_routes import predict_depression_route

app.register_blueprint(predict_depression_route, url_prefix="/api/predict")
