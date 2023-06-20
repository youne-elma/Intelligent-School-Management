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
      console.log(modal[i].info);
    }
  }

  // Make an AJAX request to the Django API endpoint
  fetch(`/api/objects/${id}/`)
    .then((response) => response.json())
    .then((data) => {
      // Process the retrieved data and update your modal and variables

      const objectInfo = data; // Assuming the entire object is returned in the API response
      console.log(objectInfo);
      // Assign the retrieved attributes to variables if needed
      const attribute1 = objectInfo.Name;
      console.log(attribute1);
      // Use the retrieved data as needed
    })
    .catch((error) => {
      console.error("Error:", error);
      // Handle error if the request fails
    });
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
