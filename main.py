from flask import Flask, request, render_template
import os
from src.utils import CNNCatDogClassification

app = Flask(__name__)

UPLOAD_FOLDER = "upload"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/uploadImage", methods=["POST"])
def uploadImage():
    if 'image_file' not in request.files:
        return "No file", 400
    
    file = request.files['image_file']

    if not allowed_file(file.filename):
        return "Invalid file type", 400

    file_name = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_name)
    obj = CNNCatDogClassification()
    result = obj.predict_cateory(file_name)
    print(result)
    if os.path.exists(file_name):
        os.remove(file_name)
    return f"{result}"

if __name__ == "__main__":
    #app.run(debug=False)
    app.run(host="0.0.0.0", port=8000)
