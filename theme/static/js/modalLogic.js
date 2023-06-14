var loadMoreButton = $('#load-more-button');

const modal = document.querySelector(".modal");
const overlay = document.querySelector(".overlay");
const openModalBtn = document.querySelectorAll(".btn-open");
const closeModalBtn = document.querySelector(".btn-close");


const openModal = function () {

  modal.classList.remove("hidden");
  overlay.classList.remove("hidden");

  var itemName = this.dataset.itemName;
  var titreAnnonce = document.getElementById('titreAnnonce');

  titreAnnonce.textContent = `"${itemName}"`;
};

openModalBtn.forEach(function(button) {
  button.addEventListener("click",openModal);
})

const closeModal = function () {
  modal.classList.add("hidden");
  overlay.classList.add("hidden");
};

closeModalBtn.addEventListener("click", closeModal);

overlay.addEventListener("click", closeModal);