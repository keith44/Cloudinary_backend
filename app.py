from flask import Flask, jsonify
import cloudinary
import cloudinary.api
import os
from dotenv import load_dotenv
app = Flask(__name__)

load_dotenv()

# Access the variables
cloud_name = os.getenv("CLOUDINARY_CLOUD_NAME")
api_key = os.getenv("CLOUDINARY_API_KEY")
api_secret = os.getenv("CLOUDINARY_API_SECRET")

# Configure Cloudinary
cloudinary.config(
  cloud_name=cloud_name,
  api_key=api_key,
  api_secret=api_secret
)

@app.route('/photos', methods=['GET'])
def get_photos():
    try:
        # Fetch all images with pagination support
        resources = cloudinary.api.resources(resource_type="image", max_results=200,context=True)
        next_cursor = resources.get("next_cursor")
        print(resources)
        photos = []
        for resource in resources['resources']:
            photos.append({
                "public_id": resource.get("public_id"),
                "secure_url": resource.get("secure_url"),
                "title": resource.get("context", {}).get("custom", {}).get("caption", "No title"),
                "description": resource.get("context", {}).get("custom", {}).get("alt", "No description")
            })
        
        # Return the photo data and the next cursor for pagination
        return jsonify({"photos": photos}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
