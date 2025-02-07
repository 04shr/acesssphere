function startMouseTracking() {
    fetch("http://your-server-ip:5000/run_streamlit")
        .then(response => response.json())
        .then(data => window.open("http://your-server-ip:8501", "_blank"))
        .catch(error => console.error("Error:", error));
}

function startVoiceRecognition() {
    fetch("http://your-server-ip:5000/run_streamlit_voice")
        .then(response => response.json())
        .then(data => window.open("http://your-server-ip:8502", "_blank"))
        .catch(error => console.error("Error:", error));
}

function startScreenReader() {
    fetch("http://your-server-ip:5000/run_streamlit_reader")
        .then(response => response.json())
        .then(data => window.open("http://your-server-ip:8503", "_blank"))
        .catch(error => console.error("Error:", error));
}

function quiz() {
  window.open("quiz.html", "_blank");
}

function riddles() {
  window.open("riddles.html", "_blank");
}
