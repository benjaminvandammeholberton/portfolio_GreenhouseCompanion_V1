const apiUrlVegetable_manager = 'http://192.168.1.104:5001/api/vegetable_manager';
let all_vegetable; 
fetch(apiUrlVegetable_manager)
.then(response => response.json())
.then(data => {
  all_vegetable = data;
  console.log(all_vegetable);
})
const apiUrlGardenArea = 'http://192.168.1.104:5001/api/garden_area';
let all_garden_area; 
fetch(apiUrlGardenArea)
.then(response => response.json())
.then(data => {
  all_garden_area = data;
  console.log(all_garden_area);
})
.catch(error => {
  console.error('Error fetching data:', error);
});




document.addEventListener("DOMContentLoaded", function(){
  console.log(all_garden_area)
});