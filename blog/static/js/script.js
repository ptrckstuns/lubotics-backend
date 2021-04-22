$(document).ready(function(){
  $("#nav-template").load("/blog/templates/nav.html");
  alert("test"); 
});


// $ (document).ready function(){
//   // $("#nav-template").load("blog/templates/nav.html");
//   alert("test);
// });

// $(document).ready(function(){
//   $("#nav-template").load("/blog/templates/nav.html");
// });

// {% include "/blog/templates/blog/nav.html" %} 

// $(document).ready( function() {
// 	$("#nav-template").load('{% url"/blog/templates/blog/nav.html" %}')
// });

//{% include "main/includes/subtemplate.html" %} 

// $(document).ready( function () {
//     $('.myClass').load('{% url update_dropdown %}',
//         {'kind': "Book" },
//         function(data){
//             alert(data);
//      });    
// });
// $(function(){
//   $("#nav-template").load(){
//   	$.ajax({
//   		url: "{% url 'blog/templates/blog/nav.html' %}",
//   	});
// }});

//alert("test"); //working
