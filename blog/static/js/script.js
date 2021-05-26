
// $(function(){
//   $("#nav-template").load("/pages/templates/nav.html");
// });
// $(function(){
//   $("#nav-footer").load("/pages/templates/footer.html");
// });


//Cart checkbox select all function
function toggleSelection(source) {
  checkboxes = document.getElementsByName("order");
  for(var i=0, n=checkboxes.length;i<n;i++) {
    checkboxes[i].checked = source.checked;
  }
  // if source.checked()
}

function singleBoxUnselect(source) {

  maincheckbox = document.querySelector('.main-checkbox')
  // para malaman ng javascript code yung main-checkbox
  
  if (maincheckbox.checked == true & source.checked == false) {
    maincheckbox.checked = false
  }
}
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
// add mo t
async function removeCartProducts() { 
  // get cart checkboxes
  checkboxes = document.getElementsByName("order");
  // loop cart checkboxes
  for(var i=0; i<checkboxes.length; i++) {
    if (checkboxes[i].checked) { // if checkboxes is checked
      // go to urls each
      console.log('checked: ', checkboxes[i].value) // print the slug
      //
      window.location.href = `/cart/remove/${checkboxes[i].value}`
      await sleep(200);
      
      // pause some
      
      // window.location.href = `/cart/remove/n1-d0`
      //click mo yung remove button
    };
    // await sleep(1000);

    window.location.href = '/cart'
    // gumana... try mo mag remove selected items mag reredirect...
  }
  // window.location.href = 'cart' 
}






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