from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/hi', methods=['GET'])
def hi():
    return jsonify({"message": "Hello!"}), 200

def run_flask():
    app.run(threaded=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

if __name__ == "__main__":
    run_flask()
