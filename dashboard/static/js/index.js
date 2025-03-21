// static/js/app.js
window.onload = function() {
    function fetchData() {
        fetch('http://127.0.0.1:8000/api/get-sensor-data/')
            .then(response => response.json())
            .then(data => {
                // Handle your data here, e.g., update Plotly graph
                console.log(data);
            });
    }

    setInterval(fetchData, 180000); // Update every 3 minutes
};
