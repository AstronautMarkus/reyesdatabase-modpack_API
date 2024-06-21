from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__)

# images folder
CAPTURES_FOLDER = 'captures'

@app.route('/captures', methods=['GET'])
def list_captures():
    files = []
    for filename in os.listdir(CAPTURES_FOLDER):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            files.append({
                'filename': filename,
                'url': f'/captures/{filename}'
            })
    return jsonify(files)

@app.route('/captures/<filename>', methods=['GET'])
def get_capture(filename):
    return send_from_directory(CAPTURES_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
