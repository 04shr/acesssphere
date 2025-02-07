function openApp(appName) {
    fetch(`/streamlit/${appName}`)
        .then(response => response.json())
        .then(data => {
            if (data.url) {
                window.open(data.url, "_blank"); // Open in a new tab
            } else {
                console.error("Error:", data.error);
            }
        })
        .catch(error => console.error("Error:", error));
}


function quiz() {
  window.open("quiz.html", "_blank");
}

function riddles() {
  window.open("riddles.html", "_blank");
}
