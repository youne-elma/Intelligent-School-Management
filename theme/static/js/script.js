const sideBar = document.getElementById("sideBar");
const mainContent = document.getElementById("mainContent")

console.log("This website was created by Youness Elmarhoum / Mohamed Baarar / Monir Chelh")
console.log("Github: youne-elma / eddev00 / mconr")

function openSidebar() {

    sideBar.classList.add("toggleNavbar");

    mainContent.addEventListener('click', function(event) {
        sideBar.classList.remove('toggleNavbar');
    });
}
        


function closeSidebar(){
    sideBar.classList.remove("toggleNavbar");
}