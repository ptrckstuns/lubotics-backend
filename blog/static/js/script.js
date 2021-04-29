
$(function(){
  $("#nav-template").load("/pages/templates/nav.html");
});
$(function(){
  $("#nav-footer").load("/pages/templates/footer.html");
});

document.querySelector('.product-small-drones').addEventListener('mouseover', () => {
  document.querySelector('#drones').classList.toggle('hide');
}) 
document.querySelector('.product-small-drones').addEventListener('mouseout', () => {
  document.querySelector('#drones').classList.toggle('hide');
}) 

document.querySelector('.product-small-education').addEventListener('mouseover', () => {
  document.querySelector('#education').classList.toggle('hide');
}) 
document.querySelector('.product-small-education').addEventListener('mouseout', () => {
  document.querySelector('#education').classList.toggle('hide');
}) 