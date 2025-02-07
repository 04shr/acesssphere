function quiz() {
  window.open("quiz.html", "_blank");
}


function riddles() {
  window.open("riddles.html", "_blank");
}

// Example API call to Flask backend (change URL to your Render backend)
fetch("https://acesssphere.onrender.com")
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));


