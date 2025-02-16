// Original functionality
function toggleReadMore(link) {
  const extraInfo = link.closest(".card").querySelector(".extra-info");
  if (extraInfo.style.display === "none" || extraInfo.style.display === "") {
    extraInfo.style.display = "block";
    link.textContent = "Read Less...";
  } else {
    extraInfo.style.display = "none";
    link.textContent = "Read More...";
  }
}

function sortProjects() {
  let projectGrid = document.getElementById("projectGrid");
  let cards = Array.from(projectGrid.getElementsByClassName("card"));
  let sortValue = document.getElementById("sortProjects").value;
  cards.sort((a, b) => {
    let nameA = a.querySelector(".project-name").textContent.toLowerCase();
    let nameB = b.querySelector(".project-name").textContent.toLowerCase();
    return sortValue === "A-Z"
      ? nameA.localeCompare(nameB)
      : nameB.localeCompare(nameA);
  });
  cards.forEach((card) => projectGrid.appendChild(card));
}

function applyFilter() {
  let filterValue = document.getElementById("statusFilter").value;
  let projectNames = document.querySelectorAll(".badge");
  projectNames.forEach((badge, index) => {
    let card = badge.closest(".card");
    if (filterValue === "all" || badge.textContent === filterValue) {
      card.style.display = "";
    } else {
      card.style.display = "none";
    }
  });
}

function openFilterDialog() {
  document.getElementById("filterDialog").style.display = "block";
  document.getElementById("filterOverlay").style.display = "block";
}

function closeFilterDialog() {
  document.getElementById("filterDialog").style.display = "none";
  document.getElementById("filterOverlay").style.display = "none";
}
// Search functionality
document
  .getElementById("searchInput")
  .addEventListener("input", function (event) {
    let filter = event.target.value.toLowerCase();
    let projectNames = document.querySelectorAll(".project-name");
    projectNames.forEach((name) => {
      let card = name.closest(".card");
      if (name.textContent.toLowerCase().includes(filter)) {
        card.style.display = "";
      } else {
        card.style.display = "none";
      }
    });
  });
