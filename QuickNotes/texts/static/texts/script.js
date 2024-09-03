window.onload = function(){

var checkbox = document.getElementById("pwdcheckbox");

var pwdfield = document.getElementById("pwdfield");

checkbox.addEventListener('change', function() {
	if(this.checked){
		pwdfield.style.display = "block";
		console.log("Lol")
	}
	else{
		pwdfield.style.display = "none";
	}	
});
};