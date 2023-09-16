document.addEventListener("DOMContentLoaded", function(){
    const sensorValueLeftElement = document.getElementById('sensor_value_left');
    const sensorValueMiddleElement = document.getElementById('sensor_value_middle');
    const sensorValueRightElement = document.getElementById('sensor_value_right');
    
    // Define the API URL you want to fetch data from
    const apiUrl = 'http://192.168.1.104:5001/api/sensors/last';

    // Fetch data from the API
    fetch(apiUrl)
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
