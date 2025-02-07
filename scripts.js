function openApp(appName) {
    fetch(`/streamlit/${appName}`)
        .then(response => response.json())
        .then(data => {
            if (data.url) {
                window.open(data.url, "_blank");
            } else {
                console.error("Error:", data.error);
                alert("Failed to open the app. Please try again.");
            }
        })
        .catch(error => console.error("Fetch error:", error));
}

function quiz() {
  window.open("quiz.html", "_blank");
}

function riddles() {
  window.open("riddles.html", "_blank");
}
