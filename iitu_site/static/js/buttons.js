
if (window.matchMedia("(max-width: 425px)").matches) {
button1 = document.getElementsByClassName("top-button")[0];
button1.style.display = "inline-block";
var bach = document.getElementById("bach");
bach.style.display = "grid";
var button2 = document.getElementsByClassName("top-button")[1];
button2.style.display = "none";
var mast = document.getElementById("mast");
mast.style.display = "none";
var button3 = document.getElementsByClassName("top-button")[2];
button3.style.display = "none";
var dock = document.getElementById("dock");
dock.style.display = "none";
} 


updateButtonListeners();

function updateButtonListeners() {
    if (button1.style.display == "inline-block" && button2.style.display == "inline-block" && button3.style.display == "inline-block") {
        button1.onclick = function() {
            hideOtherButtons(button1);
        };
        button2.onclick = function() {
            hideOtherButtons(button2);
        };
        button3.onclick = function() {
            hideOtherButtons(button3);
        };
    } else {
        button1.onclick = function() {
            showAllButtons();
        };
        button2.onclick = function() {
            showAllButtons();
        };
        button3.onclick = function() {
            showAllButtons();
        };
    }
}



function hideOtherButtons(button) {
    if (button == button1) {
        button2.style.display = "none";
        button3.style.display = "none";
        button1.classList.add("active");
        button2.classList.remove("active");
        button3.classList.remove("active");
        bach.style.display = "grid";
        mast.style.display = "none";
        dock.style.display = "none";
    } else if (button == button2) {
        button1.style.display = "none";
        button3.style.display = "none";
        button2.classList.add("active");
        button1.classList.remove("active");
        button3.classList.remove("active");
        bach.style.display = "none";
        mast.style.display = "grid";
        dock.style.display = "none";
    } else {
        button1.style.display = "none";
        button2.style.display = "none";
        button3.classList.add("active");
        button1.classList.remove("active");
        button2.classList.remove("active");
        bach.style.display = "none";
        mast.style.display = "none";
        dock.style.display = "grid";
    }
  updateButtonListeners();
}

function showAllButtons() {
    button1.style.display = "inline-block";
    button2.style.display = "inline-block";
    button3.style.display = "inline-block";
  updateButtonListeners();
}

