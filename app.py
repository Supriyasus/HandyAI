from flask import Flask, render_template, request, jsonify
import base64
import os
from utils import perform_action
import traceback

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    try:
        image_data = request.json.get('image')
        if not image_data:
            return jsonify({'error': 'No image provided'}), 400

        # Decode base64 image
        image_bytes = base64.b64decode(image_data.split(",")[1])
        temp_image_path = 'temp_image.png'
        with open(temp_image_path, 'wb') as f:
            f.write(image_bytes)

        # Detect and process gesture
        result = perform_action(temp_image_path)

        # Remove temp image
        os.remove(temp_image_path)

        return jsonify(result)

    except Exception as e:
        print("❌ ERROR:", str(e))
        print(traceback.format_exc())  # Print full error stack
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)