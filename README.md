loaded to your Cloudinary account.
Retrieves metadata such as:
Title (stored in the alt attribute).
Description (stored in the caption attribute).
Secure URL (HTTPS link to the image).
Supports pagination to handle a large number of images.
Requirements
Python 3.6+
Flask: A lightweight web framework for Python.
Cloudinary Python SDK: Used to communicate with Cloudinary’s API.
Python Dependencies
You need to install the following dependencies via pip:

```bash pip install flask cloudinary ```

Getting Started
1. Clone the Repository
```bash git clone https://github.com/yourusername/your-repo.git cd your-repo ```

2. Set Up Cloudinary
Ensure you have a Cloudinary account. If not, sign up at Cloudinary. After signing up, retrieve your cloud name, API key, and API secret from your account dashboard.

3. Set Up Environment Variables
You can either set the environment variables directly in your system or create a .env file in the project root with the following content:

```bash CLOUDINARY_CLOUD_NAME=your_cloud_name CLOUDINARY_API_KEY=your_api_key CLOUDINARY_API_SECRET=your_api_secret```

4. Run the Server
After setting up the environment variables, you can start the Flask server:

`bash python app.py `

The server will run on http://127.0.0.1:5000/photos. This endpoint will return a list of photos with their titles, descriptions, and secure URLs.

5. API Usage
Endpoint: /photos
Method: GET
Description: Retrieves all images with their titles, descriptions, and secure URLs from Cloudinary.
Example Response:
```json [ { "public_id": "sample_image_1", "secure_url": "https://res.cloudinary.com/your_cloud_name/image/upload/v1627891234/sample_image_1.jpg", "title": "Image Title 1", "description": "This is the description of image 1" }, { "public_id": "sample_image_2", "secure_url": "https://res.cloudinary.com/your_cloud_name/image/upload/v1627895678/sample_image_2.jpg", "title": "Image Title 2", "description": "This is the description of image 2" } ] ```

6. Pagination Support
If your Cloudinary account contains many images, the response will include a next_cursor to paginate through the results. You can pass this next_cursor in subsequent API requests to retrieve more images.

Contributing
Feel free to fork this project, create issues, or submit pull requests. Contributions are welcome!

License
This project does not currently have an open-source license. For any use of this code, please contact the repository owner for permissions.