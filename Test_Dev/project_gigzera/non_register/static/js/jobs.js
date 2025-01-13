const overlay = document.getElementById("overlay");
const popup = document.getElementById("popup");
const openDrawerButton1 = document.getElementById("open-drawer1");
const openDrawerButton2 = document.getElementById("open-drawer2");
const openDrawerButton3 = document.getElementById("open-drawer3");
const closeDrawerButton = document.getElementById("close-drawer");

openDrawerButton1.addEventListener("click", () => {
  overlay.classList.remove("hidden");
  popup.classList.remove("hidden");
});

openDrawerButton2.addEventListener("click", () => {
  overlay.classList.remove("hidden");
  popup.classList.remove("hidden");
});

openDrawerButton3.addEventListener("click", () => {
  overlay.classList.remove("hidden");
  popup.classList.remove("hidden");
});

closeDrawerButton.addEventListener("click", () => {
  overlay.classList.add("hidden");
  popup.classList.add("hidden");
});

// Close the drawer when clicking outside of it
overlay.addEventListener("click", (event) => {
  if (event.target === overlay) {
    overlay.classList.add("hidden");
    popup.classList.add("hidden");
  }
});

// JavaScript for video slideshow
let currentVideoIndex = 0;
const videoContainers = document.querySelectorAll(".ad-video-container");
const videos = document.querySelectorAll("video");

// Function to show the next video after the current one ends
function showNextVideo() {
  // Hide current video
  videoContainers[currentVideoIndex].classList.remove("active");

  // Move to the next video
  currentVideoIndex = (currentVideoIndex + 1) % videoContainers.length;

  // Show the next video
  videoContainers[currentVideoIndex].classList.add("active");

  // Ensure that the video starts playing when switched
  videos[currentVideoIndex].play();
}

// Attach the 'ended' event listener to each video
videos.forEach((video, index) => {
  video.addEventListener("ended", () => {
    // Show next video when the current video ends
    showNextVideo();
  });
});

// Ensure the videos are loaded and ready to play
window.addEventListener("load", () => {
  // Preload videos
  videos.forEach((video) => {
    video.load();
  });
});

// Start the slideshow when the page is loaded
window.onload = function () {
  // Start the first video
  videos[0].play();

  // Start the image slideshow
  startImageSlideshow();
};

// Function to start the image slideshow for ad-boxes
function startImageSlideshow() {
  const adBoxes = document.querySelectorAll(".ad-box .ad-slideshow");

  adBoxes.forEach((adBox) => {
    // Skip the video box (first box)
    if (adBox.querySelector(".ad-video-container")) return;

    const images = adBox.querySelectorAll(".ad-image-container");
    let activeIndex = 0;

    // Set the first image to active initially
    images[activeIndex].classList.add("active");

    // Change the active image every 3 seconds (3000 milliseconds)
    setInterval(() => {
      images[activeIndex].classList.remove("active"); // Hide the current image
      activeIndex = (activeIndex + 1) % images.length; // Move to the next image (circular)
      images[activeIndex].classList.add("active"); // Show the next image
    }, 3000); // 3 seconds interval
  });
}

// Provide quote event
document.addEventListener("DOMContentLoaded", () => {
  // Select all modal buttons and modals
  const openModalBtns = document.querySelectorAll(".openModalBtn"); // Replace id with class
  const modals = document.querySelectorAll(".quoteModal"); // Replace id with class

  // Show modal
  openModalBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      // Show the corresponding modal
      modals.forEach((modal) => modal.classList.remove("hidden"));
    });
  });

  // Loop through each modal to add close functionality
  modals.forEach((modal) => {
    const closeModalBtn = modal.querySelector(".closeModalBtn"); // Replace id with class

    // Hide modal on close button click
    closeModalBtn.addEventListener("click", () => {
      modal.classList.add("hidden");
    });

    // Hide modal when clicking outside the modal content
    modal.addEventListener("click", (e) => {
      if (e.target === modal) {
        modal.classList.add("hidden");
      }
    });
  });
});
