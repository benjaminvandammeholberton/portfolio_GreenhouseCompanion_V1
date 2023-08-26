import requests

url = "http://127.0.0.1:5000/api/v1/garden_area"
headers = {"Content-Type": "application/json"}

data = {
    "name": "Your Garden Area Name",
    "surface": 100.5
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 201:
    print("Garden area created successfully!")
    garden_area_data = response.json()
    print("Created Garden Area:")
    print("ID:", garden_area_data.get("id"))
    print("Name:", garden_area_data.get("name"))
    print("Surface:", garden_area_data.get("surface"))
else:
    print("Error:", response.text)
