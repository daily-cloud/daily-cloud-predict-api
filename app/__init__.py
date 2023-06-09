import nltk
from flask import Flask, request, jsonify

# from flask_cors import CORS

# Download NLTK data at first run
nltk.download("punkt")
nltk.download("stopwords")

UPLOAD_FOLDER = "temp"

app = Flask(__name__)
# CORS(app)
# app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


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


from app.api.routes.predict_routes import predict_image_routes, predict_text_routes

app.register_blueprint(predict_image_routes, url_prefix="/api/predict")
app.register_blueprint(predict_text_routes, url_prefix="/api/predict")
