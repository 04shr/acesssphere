function quiz() {
    window.open("quiz.html", "_blank");
}

function riddles() {
    window.open("riddles.html", "_blank");
}

// Change URL for Render Deployment
const API_BASE_URL = "https://acesssphere.onrender.com"; // Update if different

// Example API call to Flask backend
fetch(`${API_BASE_URL}/run_streamlit`)
    .then(response => response.json())
    .then(data => console.log("Backend Response:", data))
    .catch(error => console.error("Error:", error));
