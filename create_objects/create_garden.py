import requests

url = "http://127.0.0.1:5000/api/v1/garden_area"
headers = {"Content-Type": "application/json"}

# name(m), created_at(a), updated_at(a), notes, surface

data = {
    "name": "left",
    "surface": "3",
    "notes": "left side of the greenhouse"
}
keys_to_print = ["name", "surface", "notes"]
response = requests.post(url, json=data, headers=headers)

if response.status_code == 201:
    print("Garden created successfully!")
    garden_area_data = response.json()
    print("Created Garden:")
    for key in keys_to_print:
        print(f"{key.capitalize()}: {garden_area_data.get(key)}")
    print("+++++++++++++++++++++++++++")
else:
    print("Error:", response.text)
