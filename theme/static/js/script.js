const sideBar = document.getElementById("sideBar");
const mainContent = document.getElementById("mainContent")

function openSidebar() {

    sideBar.classList.add("toggleNavbar");

    mainContent.addEventListener('click', function(event) {
        sideBar.classList.remove('toggleNavbar');
    });
    
}
        
function closeSidebar(){
    sideBar.classList.remove("toggleNavbar");
}

const dropdownButton = document.querySelector('#options-menu');
const dropdownMenu = document.querySelector('#options-menu-items');

dropdownButton.addEventListener('click', (event) => {
  event.preventDefault();
  dropdownMenu.classList.toggle('hidden');
});