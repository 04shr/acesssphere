const API_BASE_URL = "http://localhost:5000";

function startStreamlitApp(endpoint) {
    fetch(`${API_BASE_URL}/${endpoint}`)
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error("Error:", error));
}

// Call functions when buttons are clicked
function runMouseTracking() {
    startStreamlitApp("run_streamlit");
}

function runVoiceRecognition() {
    startStreamlitApp("run_streamlit_voice");
}

function runScreenReader() {
    startStreamlitApp("run_streamlit_reader");
}
function quiz() {
  window.open("quiz.html", "_blank");
}

function riddles() {
  window.open("riddles.html", "_blank");
}
