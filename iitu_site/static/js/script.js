function openCity(evt, eduName) {
    // Declare all variables
    var i, tabcontent, tablinks;

    // Get all elements with class="grids-bottom-buttons" and hide them
    tabcontent = document.getElementsByClassName("grids-bottom-buttons");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Get all elements with class="top-button" and remove the class "active"
    tablinks = document.getElementsByClassName("top-button");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(eduName).style.display = "grid";
    evt.currentTarget.className += " active";
}