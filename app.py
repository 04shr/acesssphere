from flask import Flask, jsonify, send_file
from flask_cors import CORS
import subprocess
import os
import threading
import time

app = Flask(__name__)
CORS(app)

# Function to start a Streamlit app on a given port
def start_streamlit(script_name, port):
    def run():
        os.system(f"streamlit run {script_name} --server.port {port} --server.headless true")
    
    thread = threading.Thread(target=run, daemon=True)
    thread.start()
    time.sleep(3)  # Give some time for the Streamlit app to start
    return f"http://localhost:{port}"

# Routes to start different Streamlit apps
@app.route('/run_streamlit', methods=['GET'])
def run_mouse_tracking():
    url = start_streamlit("hands_free_mouse.py", 8501)
    return jsonify({"status": "success", "url": url})

@app.route('/run_streamlit_voice', methods=['GET'])
def run_voice_recognition():
    url = start_streamlit("voice_recognition.py", 8502)
    return jsonify({"status": "success", "url": url})

@app.route('/run_streamlit_reader', methods=['GET'])
def run_screen_reader():
    url = start_streamlit("screen_reader.py", 8503)
    return jsonify({"status": "success", "url": url})

# Serve HTML files
@app.route('/')
def serve_index():
    return send_file("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
