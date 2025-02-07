from flask import Flask, jsonify, request
from flask_cors import CORS
import subprocess
import time

app = Flask(__name__)
CORS(app)

# Function to start Streamlit apps and wait for them to become available
def start_streamlit(script_name, port):
    try:
        subprocess.Popen(
            ['streamlit', 'run', script_name, '--server.port', str(port), '--server.headless', 'true'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        time.sleep(3)  # Wait for Streamlit to start
        return jsonify({"status": "success", "message": f"{script_name} is running on port {port}"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

# Routes to start each Streamlit app
@app.route('/run_streamlit', methods=['GET'])
def run_streamlit():
    return start_streamlit('hands_free_mouse.py', 5001)

@app.route('/run_streamlit_voice', methods=['GET'])
def run_streamlit_voice():
    return start_streamlit('voice_recognition.py', 5002)

@app.route('/run_streamlit_reader', methods=['GET'])
def run_streamlit_reader():
    return start_streamlit('screen_reader.py', 5003)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
