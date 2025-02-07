from flask import Flask, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Enable access from any device

# Function to start a Streamlit app
def start_streamlit_app(script_name, port):
    try:
        subprocess.Popen(["streamlit", "run", script_name, "--server.port", str(port), "--server.headless", "true"])
        return jsonify({"status": "success", "message": f"{script_name} is running on port {port}"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

# Routes to launch different Streamlit apps
@app.route('/run_streamlit', methods=['GET'])
def run_streamlit():
    return start_streamlit_app("hands_free_mouse.py", 8501)

@app.route('/run_streamlit_voice', methods=['GET'])
def run_streamlit_voice():
    return start_streamlit_app("voice_recognition.py", 8502)

@app.route('/run_streamlit_reader', methods=['GET'])
def run_streamlit_reader():
    return start_streamlit_app("screen_reader.py", 8503)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)  # Make Flask accessible from any device
