var form = document.getElementById("my_form");
var elements = form.elements;
for (var i = 0, len = elements.length; i < len; ++i) {
    elements[i].readOnly = true;
}

var submit_btn= document.getElementById("submit_btn");
submit_btn.hidden= true;
var cancel_btn= document.getElementById("cancel_btn");
cancel_btn.hidden= true;


var edit_btn= document.getElementById("edit_btn");

edit_btn.addEventListener('click', event => {
	for (var i = 0, len = elements.length; i < len; ++i) {
    	    elements[i].readOnly = false;}
	submit_btn.hidden= false;
	cancel_btn.hidden=false;

 
	
});



