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

import {
    Carousel,
    initTE,
  } from "tw-elements";
  
  initTE({ Carousel });

  

// Initialization for ES Users
import {
    Carousel,
    initTE,
  } from "tw-elements";
  
  initTE({ Carousel });