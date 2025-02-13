function sendMessage() {
  const input = document.getElementById("chat-input");
  const message = input.value.trim();

  if (message) {
    const chatMessages = document.getElementById("chat-messages");
    const userMessage = document.createElement("div");

    userMessage.classList.add(
      "flex",
      "items-start",
      "justify-start",
      "space-x-3"
    );
    userMessage.innerHTML = `
      <img src="https://storage.googleapis.com/uxpilot-auth.appspot.com/avatars/avatar-1.jpg" class="w-8 h-8 rounded-full">
        <div class="bg-blue-100 rounded-lg p-3">
          <p class="text-sm text-blue-800">${message}</p>
        </div>
      `;

    chatMessages.appendChild(userMessage);
    chatMessages.scrollTop = chatMessages.scrollHeight;
    input.value = "";
  }
}

document.getElementById("chat-send").addEventListener("click", sendMessage);

document
  .getElementById("chat-input")
  .addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
      sendMessage();
    }
  });

//  JavaScript for Modal  of financial overiview
function openModal1() {
  console.log("I am inside the openmodal-13");
  document.getElementById("financialModal").classList.remove("hidden");
  document.getElementById("financialModal").classList.add("flex");
}

function closeModal1() {
  document.getElementById("financialModal").classList.add("hidden");
  document.getElementById("financialModal").classList.remove("flex");
}

// JavaScript for Modal Toggle  for board cast messages email whatsup sms
function openModal(id) {
  // Close the broadcast modal when opening another modal
  closeModal("broadcastModal");

  // Hide all other modals before opening the selected one
  const allModals = ["emailModal", "whatsappModal", "smsModal"];
  allModals.forEach((modal) => {
    if (modal !== id) {
      closeModal(modal);
    }
  });

  // Open the selected modal
  document.getElementById(id).classList.remove("hidden");
  document.getElementById(id).classList.add("flex");
}

function closeModal(id) {
  document.getElementById(id).classList.add("hidden");
  document.getElementById(id).classList.remove("flex");
}

// Close modal when clicking outside of it
window.addEventListener("click", function (event) {
  const allModals = [
    "broadcastModal",
    "emailModal",
    "whatsappModal",
    "smsModal",
  ];
  allModals.forEach((modalId) => {
    const modal = document.getElementById(modalId);
    if (
      modal &&
      !modal.classList.contains("hidden") &&
      event.target === modal
    ) {
      closeModal(modalId);
    }
  });
});

// JavaScript for Reports Modal
function openDownloadModal() {
  document.getElementById("reportsDownloadModal").classList.remove("hidden");
  document.getElementById("reportsDownloadModal").classList.add("flex");
}

function closeDownloadModal() {
  document.getElementById("reportsDownloadModal").classList.add("hidden");
  document.getElementById("reportsDownloadModal").classList.remove("flex");
}
