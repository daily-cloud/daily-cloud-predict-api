from flask import Flask, jsonify
from flask_cors import CORS

UPLOAD_FOLDER = "temp"

app = Flask(__name__)
CORS(app)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def index():
    return jsonify({"message": "Welcome to Daily Cloud Predict API", "version": "0.1.0"}), 200

from app.api.routes.predict_routes import predict_image_routes, predict_text_routes

app.register_blueprint(predict_image_routes, url_prefix="/api/predict")
app.register_blueprint(predict_text_routes, url_prefix="/api/predic")