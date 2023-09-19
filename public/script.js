document.addEventListener("DOMContentLoaded", function(){
    const sensorValueLeftElement = document.getElementById('sensor_value_left');
    const sensorValueMiddleElement = document.getElementById('sensor_value_middle');
    const sensorValueRightElement = document.getElementById('sensor_value_right');
    
    // Define the API URL you want to fetch data from
    const apiUrl = 'https://5259-2a02-8440-721b-2ea0-d173-97af-8f29-289.ngrok-free.app/api/sensors/last';
    // Define headers to include in the request
    const headers = new Headers();
    headers.append('ngrok-skip-browser-warning', '1'); // Set the ngrok-skip-browser-warning header

    // Fetch data from the API with headers
    fetch(apiUrl, {
        method: 'GET',
        headers: headers
    })
        .then(response => response.json()) // Assuming the API returns JSON data
        .then(data => {
            const soilHumidity1Value = data.soil_humidity_1;
            const soilHumidity2Value = data.soil_humidity_2;
            const soilHumidity3Value = data.soil_humidity_3;
            sensorValueLeftElement.textContent = `${soilHumidity1Value}`;
            sensorValueMiddleElement.textContent = `${soilHumidity2Value}`;
            sensorValueRightElement.textContent = `${soilHumidity3Value}`;
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
});
