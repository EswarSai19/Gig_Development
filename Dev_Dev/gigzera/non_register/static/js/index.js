let slideIndex = 1; // Start with the first slide (index is 1-based)
let slideTimer; // Store the timeout reference for auto-slide
let isNavigating = false; // Prevent rapid navigation

function showSlides() {
  const slides = document.querySelectorAll(".slide");
  const counter = document.querySelector(".counter");

  // Ensure slideIndex wraps around
  if (slideIndex > slides.length) slideIndex = 1;
  if (slideIndex < 1) slideIndex = slides.length;

  // Hide all slides
  slides.forEach((slide) => (slide.style.display = "none"));

  // Show the current slide
  slides[slideIndex - 1].style.display = "block";

  // Update the counter
  if (counter) {
    counter.textContent = `${slideIndex
      .toString()
      .padStart(2, "0")}/${slides.length.toString().padStart(2, "0")}`;
  }

  // Automatically switch to the next slide after 4 seconds
  slideTimer = setTimeout(() => {
    slideIndex++;
    showSlides();
  }, 4000); // 4-second interval
}

function changeSlide(direction) {
  if (isNavigating) return; // Prevent rapid navigation

  isNavigating = true; // Set navigation lock
  clearTimeout(slideTimer); // Stop the automatic slideshow

  slideIndex += direction; // Adjust the slide index based on direction
  showSlides(); // Show the new slide immediately

  // Allow new navigation after a short delay
  setTimeout(() => {
    isNavigating = false; // Release the navigation lock
  }, 300); // 300ms lock duration
}

// Initialize the slideshow on page load
document.addEventListener("DOMContentLoaded", () => {
  showSlides();

  // Attach event listeners to navigation buttons (if they exist)
  const prevButton = document.querySelector(".prev");
  const nextButton = document.querySelector(".next");

  if (prevButton) {
    prevButton.addEventListener("click", () => changeSlide(-1));
  }

  if (nextButton) {
    nextButton.addEventListener("click", () => changeSlide(1));
  }
});

// start
// pop up js code for contact us
document.addEventListener("DOMContentLoaded", function () {
  const contactBtn = document.getElementById("contactBtn");
  const contactBtn2 = document.getElementById("contactBtn2");
  const popupPanel = document.getElementById("popupPanel");
  const popupOverlay = document.getElementById("popupOverlay");
  const closeBtn = document.getElementById("closeBtn");

  // Function to open sidebar
  contactBtn.onclick = function () {
    popupOverlay.style.display = "block"; // Show overlay
    popupPanel.style.right = "0"; // Slide in sidebar
  };
  contactBtn2.onclick = function () {
    popupOverlay.style.display = "block"; // Show overlay
    popupPanel.style.right = "0"; // Slide in sidebar
  };
  // Function to close sidebar
  function closeSidebar() {
    popupOverlay.style.display = "none"; // Hide overlay
    popupPanel.style.right = "-400px"; // Slide out sidebar
  }

  closeBtn.onclick = closeSidebar;

  // Close sidebar when clicking outside
  popupOverlay.onclick = function (e) {
    if (e.target === popupOverlay) {
      closeSidebar();
    }
  };
});
//end of pop up js code
