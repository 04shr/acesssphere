from flask import Flask, render_template, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Function to run Streamlit apps
def run_streamlit(script_name, port):
    return subprocess.Popen(["streamlit", "run", script_name, "--server.port", str(port), "--server.headless", "true"])

# Start Streamlit Apps
streamlit_processes = {
    "mouse_tracking": run_streamlit("hands_free_mouse.py", 8501),
    "voice_assistant": run_streamlit("voice_recognition.py", 8502),
    "screen_reader": run_streamlit("screen_reader.py", 8503),
}

@app.route("/")
def home():
    return render_template("index.html")  # Ensure you have an index.html

@app.route("/streamlit/<app_name>")
def open_streamlit(app_name):
    ports = {"mouse_tracking": 8501, "voice_assistant": 8502, "screen_reader": 8503}
    if app_name in ports:
        return jsonify({"url": f"http://localhost:{ports[app_name]}"})
    return jsonify({"error": "Invalid app name"}), 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)  # Accessible from any device
