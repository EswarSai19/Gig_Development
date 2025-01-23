// pop up js code for contact us
document.addEventListener("DOMContentLoaded", function () {
  const contactBtn = document.getElementById("contactBtn");
  // const contactBtn3 = document.getElementById("contactBtn3");
  const popupPanel = document.getElementById("popupPanel");
  const popupOverlay = document.getElementById("popupOverlay");
  const closeBtn = document.getElementById("closeBtn");

  // Function to open sidebar
  contactBtn.onclick = function () {
    popupOverlay.style.display = "block"; // Show overlay
    popupPanel.style.right = "0"; // Slide in sidebar
  };
  // contactBtn3.onclick = function () {
  //   popupOverlay.style.display = "block"; // Show overlay
  //   popupPanel.style.right = "0"; // Slide in sidebar
  // };
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
