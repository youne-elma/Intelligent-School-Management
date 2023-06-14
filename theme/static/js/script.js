const sideBar = document.getElementById("sideBar");
const mainContent = document.getElementById("mainContent")

console.log("This website was created by Monir Chelh / Mohamed Baarar / Youness Elmarhoum")
console.log("Github: mconr / eddev00 / youne-elma")

function openSidebar() {

    sideBar.classList.add("toggleNavbar");

    mainContent.addEventListener('click', function(event) {
        sideBar.classList.remove('toggleNavbar');
    });
}
        


function closeSidebar(){
    sideBar.classList.remove("toggleNavbar");
}