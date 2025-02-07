from flask import Flask, jsonify, render_template
import subprocess

app = Flask(__name__)

# Define Streamlit apps and their ports
STREAMLIT_APPS = {
    "hands_free_mouse": 8501,
    "voice_recognition": 8502,
    "screen_reader": 8503,
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/streamlit/<app_name>")
def open_streamlit(app_name):
    if app_name in STREAMLIT_APPS:
        url = f"http://localhost:{STREAMLIT_APPS[app_name]}"
        return jsonify({"url": url})
    return jsonify({"error": "Invalid app name"}), 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
