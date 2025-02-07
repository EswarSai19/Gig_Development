from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Route to render the HTML page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload-image', methods=['POST'])
def upload_image():
    # Get the uploaded file from the form
    file = request.files['file']

    # AWS API endpoint to upload the file to S3
    api_url = 'https://88qmxi59qe.execute-api.ap-south-1.amazonaws.com/Sandbox/jobs-sec1-ads/www_postman_com'

    # Set the content type to image/jpeg
    headers = {'Content-Type': 'image/jpeg'}

    # Make the PUT request to upload the file to AWS S3
    response = requests.put(api_url, headers=headers, data=file.read())

    # Check the response status and return appropriate message
    if response.status_code == 200:
        return jsonify({'message': 'File uploaded successfully!', 'status': 'success'}), 200
    else:
        return jsonify({'message': 'Failed to upload file.', 'status': 'error'}), 400

if __name__ == '__main__':
    app.run(debug=True)
