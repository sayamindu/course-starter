// Bunch of workarounds to better integrate Pandoc output within Bootstrap

/*
   Integrate table of contents into the top navbar
   https://stackoverflow.com/a/60742588
*/

var navbarList = document.querySelector('#navbarContent ul');

if (navbarList) {
    navbarList.classList.add('navbar-nav', 'ml-auto');
    document.querySelectorAll('.navbar-nav li').forEach(function(navItem){
        navItem.classList.add('navbar-item');
        if (navItem.firstChild.nodeName == 'A') {
            navItem.firstChild.classList.add('nav-link');
        };
    });
}

// Deal with tables
var tables = document.querySelectorAll('.container table')

tables.forEach(function(table) {
    table.classList.add('table', 'table-bordered', 'table-striped', 'table-sm');
});


window.addEventListener("hashchange", function() { scrollBy(0, -65) })
