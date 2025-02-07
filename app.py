from flask import Flask, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

@app.route('/run_streamlit', methods=['GET'])
def run_streamlit():
    try:
        subprocess.Popen(['streamlit', 'run', 'hands_free_mouse.py', '--server.port=5000'])
        return jsonify({"status": "success", "message": "Streamlit app is running on port 5000"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/run_streamlit_voice', methods=['GET'])
def run_streamlit_voice():
    try:
        subprocess.Popen(['streamlit', 'run', 'voice_recognition.py', '--server.port=5001'])
        return jsonify({"status": "success", "message": "Voice Streamlit app is running on port 5001"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/run_streamlit_reader', methods=['GET'])
def run_streamlit_reader():
    try:
        subprocess.Popen(['streamlit', 'run', 'screen_reader.py', '--server.port=5002'])
        return jsonify({"status": "success", "message": "Reader Streamlit app is running on port 5002"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)  # Allow external access
