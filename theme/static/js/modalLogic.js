const modal = document.querySelectorAll(".modal");
const overlay = document.querySelectorAll(".overlay");
const openModalBtn = document.querySelectorAll(".btn-open");
const closeModalBtn = document.querySelectorAll(".btn-close");

const openModal = function (id) {
  console.log(id);
  for (let i = 0; i < modal.length; i++) {
    if (modal[i].id == id) {
      modal[i].classList.remove("hidden");
      overlay[i].classList.remove("hidden");
    }
  }
};

openModalBtn.forEach(function (button) {
  button.addEventListener("click", function () {
    openModal(button.id);
  });
});

const closeModal = function () {
  modal.forEach(function (modal) {
    modal.classList.add("hidden");
  });

  overlay.forEach(function (overlay) {
    overlay.classList.add("hidden");
  });
};

closeModalBtn.forEach((button) => {
  button.addEventListener("click", closeModal);
});

overlay.forEach((overlay) => {
  overlay.addEventListener("click", closeModal);
});
