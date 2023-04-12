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
