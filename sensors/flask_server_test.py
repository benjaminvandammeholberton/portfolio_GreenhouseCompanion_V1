from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)


@app.route('/api/endpoint', methods=['POST'])
def receive_data():
    if request.method == 'POST':
        data = request.get_json()
        data["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Create a new dictionary to store the modified data
        modified_data = data.copy()

        # Specify the file path where you want to save the JSON data
        file_path = 'data.json'

        try:
            with open(file_path, 'r') as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            # If the file doesn't exist, initialize existing_data as an empty list or dictionary
            existing_data = []

        # Step 2: Add the new data to the existing JSON data
        existing_data.append(data)

        # Step 3: Write the updated JSON data back to the file
        with open(file_path, 'w') as file:
            json.dump(existing_data, file, indent=4)

        for key, value in data.items():
            if key in ["sensor_1", "sensor_2", "sensor_3"] and int(value) > 2500:
                modified_data['relay'] = True

        # Return the modified data as JSON
        print(modified_data)
        return jsonify(modified_data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
