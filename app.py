from flask import Flask, request, jsonify
import cloudinary
import cloudinary.uploader
import cloudinary.api


from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
cloud_name = os.getenv("CLOUDINARY_CLOUD_NAME")
api_key = os.getenv("CLOUDINARY_API_KEY")
api_secret = os.getenv("CLOUDINARY_API_SECRET")

app = Flask(__name__)


# Configure Cloudinary
cloudinary.config(
  cloud_name=cloud_name,
  api_key=api_key,
  api_secret=api_secret
)



@app.route("/upload", methods=["POST"])
def upload_file():
    # Check if the request has the file part
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    
    # Upload the file to Cloudinary
    try:
        result = cloudinary.uploader.upload(file, folder="user_uploads", context="caption=Uploaded from Android App")
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Retrieve resource details (by public_id)
@app.route("/resource/<public_id>", methods=["GET"])
def get_resource(public_id):
    try:
        result = cloudinary.api.resource(public_id)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
