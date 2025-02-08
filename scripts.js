function quiz() {
  window.open("quiz.html", "_blank");
}

function riddles() {
  window.open("riddles.html", "_blank");
}

const API_BASE_URL = "https://acesssphere.onrender.com";  // Change this to your Render API URL

function startStreamlitApp(endpoint) {
    fetch(`${API_BASE_URL}/${endpoint}`)
        .then(response => response.json())
        .then(data => {
            if (data.status === "success") {
                console.log(data.message);
                alert(data.message);
            } else {
                console.error("Error:", data.message);
                alert("Error starting app: " + data.message);
            }
        })
        .catch(error => {
            console.error("Fetch error:", error);
            alert("Could not connect to server.");
        });
}

function runMouseTracking() {
    startStreamlitApp("run_streamlit");
}

function runVoiceRecognition() {
    startStreamlitApp("run_streamlit_voice");
}

function runScreenReader() {
    startStreamlitApp("run_streamlit_reader");
}

