function toggleFilterPopup() {
  const popup = document.getElementById("filter-popup");
  const overlay = document.getElementById("blur-overlay");

  // Toggle visibility of the filter pop-up and background blur
  const isHidden = popup.classList.contains("hidden");
  if (isHidden) {
    popup.classList.remove("hidden");
    overlay.classList.add("active");
  } else {
    popup.classList.add("hidden");
    overlay.classList.remove("active");
  }
}

function closeFilterPopup() {
  const popup = document.getElementById("filter-popup");
  const overlay = document.getElementById("blur-overlay");

  popup.classList.add("hidden");
  overlay.classList.remove("active");
}

function filterProjects() {
  const searchQuery = document
    .getElementById("search-input")
    .value.toLowerCase();
  const selectedStatus = document.getElementById("status-filter").value;
  const sortOrder = document.getElementById("sort-filter").value;

  const projectsContainer = document.querySelector(".projects");
  const projects = Array.from(
    projectsContainer.querySelectorAll(".project-box")
  );

  // Sort projects by title (A-Z or Z-A)
  const sortedProjects = projects.sort((a, b) => {
    const titleA = a.querySelector("h2").textContent.trim().toLowerCase();
    const titleB = b.querySelector("h2").textContent.trim().toLowerCase();

    if (sortOrder === "a-z") {
      return titleA.localeCompare(titleB);
    } else if (sortOrder === "z-a") {
      return titleB.localeCompare(titleA);
    }
    return 0; // No sorting if no option selected
  });

  // Loop through sorted projects and display/hide based on search and status filters
  sortedProjects.forEach((project) => {
    const title = project.querySelector("h2").textContent.toLowerCase();
    const status = project.querySelector(".status").classList[1];

    // Check if the project matches the search query and selected filters
    const matchesSearch = title.includes(searchQuery);
    const matchesStatus = selectedStatus ? status === selectedStatus : true;

    // Display or hide the project based on the filters
    if (matchesSearch && matchesStatus) {
      project.style.display = "block";
    } else {
      project.style.display = "none";
    }
  });

  // Re-append sorted projects to the container to ensure they appear in the correct order
  sortedProjects.forEach((project) => {
    projectsContainer.appendChild(project);
  });
}

function readMoreDetails(opportunityId) {
  const box = document.querySelector(
    `.project-box[data-id="${opportunityId}"]`
  );
  const link = box.querySelector("a");

  // Toggle the expanded class
  box.classList.toggle("expanded");

  // Change the link text based on the expanded state
  if (box.classList.contains("expanded")) {
    link.textContent = "Read Less...";
  } else {
    link.textContent = "Read More...";
  }
}

function viewOverallStatus(opportunityId) {
  window.location.href = `/project-overall-status/${opportunityId}`;
}
