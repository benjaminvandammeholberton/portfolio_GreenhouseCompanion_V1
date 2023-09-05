from models.garden_area import GardenArea
from models.vegetable_manager import VegetableManager
from models import storage


gardens = [
    GardenArea(name="left", surface=2.5),
    GardenArea(name="middle", surface=2.5),
    GardenArea(name="right", surface=2.5),
    GardenArea(name="back", surface=2.5)
]
vegetables = [
    VegetableManager(name="tomato", notes="tomato organic", quantity=3),
    VegetableManager(name="carrot", notes="carrot organic", quantity=3),
    VegetableManager(name="spinach", notes="spinach organic", quantity=3),
]

for garden in gardens:
    storage.new(garden)

for vegetable in vegetables:
    storage.new(vegetable)

storage.save()
