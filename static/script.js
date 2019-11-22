//toggle mobile nav class 
var nav = document.querySelector("nav ul"),
navToggle = document.querySelector("nav .skip");
if (navToggle) {
	navToggle.addEventListener("click", function(a) {
		if (nav.className == "open") {
			nav.className = "";
		} else {
			nav.className = "open";
		}
		a.preventDefault();
	}, false);
}

//toggle nav when page is clicked
var specifiedElement = document.querySelector('nav');
document.addEventListener('click', function(event) {
	var isClickInside = specifiedElement.contains(event.target);
	if (!isClickInside && nav.className == "open") {
    nav.className = "";
	} 
});

//detect colour scheme and set checkbox
var checkBox = document.getElementById("schemeCheck");
var checkLabel = document.getElementById("schemeLabel");
function detectScheme() {
	var theme = "light";
    if(localStorage.getItem("theme")) {
        if(localStorage.getItem("theme") == "dark") {
            var theme = "dark";
        }
    } else if(!window.matchMedia) {
        return false;
    } else if(window.matchMedia("(prefers-color-scheme: dark)").matches) {
		var theme = "dark";
    }
    if (theme=="dark") {
         document.documentElement.setAttribute("data-theme", "dark");
		 checkBox.checked = false;
    } else {
		 checkBox.checked = true;
	}
	if (document.documentElement.getAttribute("data-theme") == "dark"){
		checkBox.checked = true;
	} else {
		checkBox.checked = false;
	}
}
detectScheme();

// toggle dark mode
checkBox.addEventListener("change", darkMode, false);

function darkMode() {
	if (checkBox.checked == true){
		localStorage.setItem("theme", "dark");
		document.documentElement.setAttribute('data-theme', 'dark');
	} else {
		localStorage.setItem('theme', 'light');
        document.documentElement.setAttribute('data-theme', 'light');
	}
}

// prevent enter from submitting forms
document.querySelector("form").onkeypress = function(e) {
	var key = e.charCode || e.keyCode || 0;     
	if (key == 13) {
	  e.preventDefault();
	}
  }

// hide alert
var hideAlert = document.querySelector("#alert-close");
if (hideAlert) {
	hideAlert.addEventListener("click", function(e) {
		var alertDiv = document.querySelector("#alert");
		if (alertDiv.style.display === "none") {
			alertDiv.style.display = "block";
		} else {
			alertDiv.style.display = "none";
		}
	}, false);
}

// tagging system for blog
const tagContainer = document.querySelector('.tag-container');
const input = document.querySelector('.tag-container input');
let tags = [];
function createTag(label) {
	const div = document.createElement('div');
	div.setAttribute('class', 'tag');
	const span = document.createElement('span');
	span.innerHTML = label;
	const closeIcon = document.createElement('a');
	closeIcon.innerHTML = ' x';
	closeIcon.setAttribute('class', 'tag-close');
	closeIcon.setAttribute('data-item', label);
	div.appendChild(span);
	div.appendChild(closeIcon);
	return div;
}

function clearTags() {
	document.querySelectorAll('.tag').forEach(tag => {
		tag.parentElement.removeChild(tag);
	});
}

function addTags() {
	clearTags();
	tags.slice().reverse().forEach(tag => {
		tagContainer.prepend(createTag(tag));
	});
}

input.addEventListener('keyup', (e) => {
    if (e.key === "Enter") {
		if ((input && input.value) && ( new RegExp("[^\s" + "," + "]").test(input.value) && 
		(!input.value.startsWith(",") || !input.value.endsWith(",")) )
		){
        	e.target.value.split(',').forEach(tag => {
			tags.push(tag);  
        	});
        	addTags();
        	input.value = '';
		}
	}
});

document.addEventListener('click', (e) => {
	//console.log(e.target.tagName);
	if (e.target.tagName === 'A') {
		const tagLabel = e.target.getAttribute('data-item');
		const index = tags.indexOf(tagLabel);
		tags = [...tags.slice(0, index), ...tags.slice(index+1)];
		addTags();    
	}
})

//example tags
tags = ["some", "tags"];
addTags();  

