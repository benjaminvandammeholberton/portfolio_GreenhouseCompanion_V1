import requests
import json

url = "http://127.0.0.1:5001/api/v1/vegetable_manager"
headers = {"Content-Type": "application/json"}

# name, sowed, planted, sowing_date, planting_date,
# harvest_date, remove_date, harvest_quantity, notes,
# garden_area_id

# date format : YYYY-MM-DD
keys_to_print = ["name", "garden_area_id",  "created_at",  "updated_at", "sowed", "planted", "sowing_date",
                 "planting_date", "harvest_date", "remove_date", "harvest_quantity", "notes"]

with open("data.json", "r") as file:
    data = json.load(file)
for item in data:
    print(item)

    response = requests.post(url, json=item, headers=headers)

    if response.status_code == 201:
        print("Vegetable created successfully!")
        vegetable_data = response.json()
        print("Created Vegetable:")
        for key in keys_to_print:
            print(f"{key.capitalize()}: {vegetable_data.get(key)}")
        print("+++++++++++++++++++++++++++")
    else:
        print("Error:", response.text)
