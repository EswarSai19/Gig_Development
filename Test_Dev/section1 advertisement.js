// Function to save advertisement in the respective section
function saveAdvertisement(section) {
  const mediaTypeElement = document.getElementById(`mediaType${section}`);
  const mediaType = mediaTypeElement.value;
  const redirectInput = document.getElementById(`redirectLink${section}`);
  const redirectUrl = redirectInput ? redirectInput.value.trim() : "";

  const fileInput = document.getElementById(`fileInput${section}`);
  const file = fileInput.files[0];

  if (!file) {
    alert("Please select a media file.");
    return;
  }

  const tableBody = document.querySelector(
    `#section${section} .ad-table tbody`
  );
  if (!tableBody) {
    console.error(`Table body for section ${section} not found.`);
    return;
  }

  const serialNumber = tableBody.rows.length + 1;
  const mediaTypeIcon =
    mediaType === "Video"
      ? '<i class="fas fa-video"></i>'
      : '<i class="fas fa-image"></i>';

  const newRow = document.createElement("tr");
  newRow.innerHTML = `
    <td>${serialNumber}.</td>
    <td>${mediaTypeIcon} ${mediaType}</td>
    <td>${file.name}</td>
    <td>${redirectUrl || "No redirect link"}</td>
    <td>
      <button class="edit-button btn btn-secondary btn-sm" onclick="editRow(this)">
        <i class="fas fa-edit"></i> Edit
      </button>
      <button class="delete-button btn btn-danger btn-sm" onclick="deleteRow(this)">
        <i class="fas fa-trash-alt"></i> Delete
      </button>
    </td>
  `;

  tableBody.appendChild(newRow);

 

  // Clear form
  fileInput.value = "";
  if (redirectInput) redirectInput.value = "";
  updateFileNameDisplay(section, "No file selected");

  // Close modal
  closeModal(`createAdModal${section}`);

  alert("Advertisement added successfully!");
}

// Function to update the file input type based on media type selection
function updateFileType(section) {
  const mediaType = document.getElementById(`mediaType${section}`).value;
  const fileInput = document.getElementById(`fileInput${section}`);

  if (mediaType === "Video") {
    fileInput.setAttribute("accept", "video/*");
  } else {
    fileInput.setAttribute("accept", "image/*");
  }

  // Reset the file input if the user changes the media type after selecting a file
  fileInput.value = "";
  updateFileNameDisplay(section, "No file selected");
}


// Function to handle drag and drop area
function handleDragOver(event) {
  event.preventDefault();
  const dragArea = event.currentTarget;
  dragArea.classList.add("bg-gray-100");
}

// Function to handle drag leave
function handleDragLeave(event) {
  event.preventDefault();
  const dragArea = event.currentTarget;
  dragArea.classList.remove("bg-gray-100");
}

// Function to handle dropped files
function handleDrop(event, section) {
  event.preventDefault();
  const dragArea = event.currentTarget;
  dragArea.classList.remove("bg-gray-100");

  const fileInput = document.getElementById(`fileInput${section}`);
  const files = event.dataTransfer.files;

  if (files.length > 0) {
    fileInput.files = files;
    updateFileNameDisplay(section, files[0].name);
  }
}

// Function to handle manual file selection
function handleFileSelect(event, section) {
  const fileInput = event.target;
  const file = fileInput.files[0];
  const mediaType = document.getElementById(`mediaType${section}`).value;

  if (file) {
    const fileType = file.type;

    if (
      (mediaType === "Image" && !fileType.startsWith("image/")) ||
      (mediaType === "Video" && !fileType.startsWith("video/"))
    ) {
      alert(`Please select a valid ${mediaType.toLowerCase()} file.`);
      fileInput.value = ""; // Clear the invalid file selection
      updateFileNameDisplay(section, "No file selected");
      return;
    }

    updateFileNameDisplay(section, file.name);
  }
}


// Function to trigger the file input click manually
function triggerFileInput(section) {
  const fileInput = document.getElementById(`fileInput${section}`);
  fileInput.click();
}

// Function to update the file name display area
function updateFileNameDisplay(section, fileName) {
  const fileNameDisplay = document.getElementById(`fileName${section}`);
  if (fileNameDisplay) {
    fileNameDisplay.innerHTML =
      fileName === "No file selected" ? fileName : `Selected File: ${fileName}`;
  }
}

// Function to delete a row
function deleteRow(button) {
  if (confirm("Are you sure you want to delete this advertisement?")) {
    const row = button.closest("tr");
    const tableBody = row.closest("tbody");

    row.remove();

    // Update serial numbers
    Array.from(tableBody.rows).forEach((row, index) => {
      row.cells[0].innerText = `${index + 1}.`;
    });
  }
}

// Function to edit a row
function editRow(button) {
  const row = button.closest("tr");
  const fileNameCell = row.cells[2];
  const redirectLinkCell = row.cells[3];
  const currentFileName = fileNameCell.innerText.trim();
  const currentRedirectLink = redirectLinkCell.innerText.trim();

  // Show the Edit Modal
  const modal = document.getElementById("editMediaModal");
  modal.classList.remove("hidden");

  // Add redirect link input if not exists
  const modalBody = modal.querySelector(".p-6");
  if (!document.getElementById("editRedirectLink")) {
    modalBody.insertAdjacentHTML(
      "beforeend",
      `
      <div class="mt-4">
        <label for="editRedirectLink" class="block text-sm font-medium text-gray-700">Redirect Link</label>
        <input type="url" id="editRedirectLink" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500">
      </div>
    `
    );
  }

  // Set up existing values
  const fileInput = document.getElementById("editFileInput");
  const fileNameDisplay = document.getElementById("editFileNameDisplay");
  const redirectInput = document.getElementById("editRedirectLink");

  fileNameDisplay.textContent = `Current File: ${currentFileName}`;
  if (redirectInput && currentRedirectLink !== "No redirect link") {
    redirectInput.value = currentRedirectLink;
  }

  // Handle Save Button
  const saveButton = document.getElementById("saveEditedFile");
  saveButton.onclick = function () {
    const selectedFile = fileInput.files[0];
    const newRedirectLink = redirectInput ? redirectInput.value.trim() : "";

    // Update file name if new file selected
    if (selectedFile) {
      fileNameCell.innerText = selectedFile.name;
    }

    // Update redirect link
    redirectLinkCell.innerText = newRedirectLink || "No redirect link";

    closeEditModal();
    alert("Advertisement updated successfully!");
  };
}

// Function to close edit modal
function closeEditModal() {
  const modal = document.getElementById("editMediaModal");
  const fileInput = document.getElementById("editFileInput");
  const redirectInput = document.getElementById("editRedirectLink");
  const fileNameDisplay = document.getElementById("editFileNameDisplay");

  // Clear inputs
  if (fileInput) fileInput.value = "";
  if (redirectInput) redirectInput.value = "";
  if (fileNameDisplay) fileNameDisplay.textContent = "No file selected";

  modal.classList.add("hidden");
}

// Initialize event listeners when document is ready
document.addEventListener("DOMContentLoaded", function () {
  // Add dragover and dragleave listeners to all drag-drop areas
  document.querySelectorAll(".drag-drop-area").forEach((area) => {
    area.addEventListener("dragover", handleDragOver);
    area.addEventListener("dragleave", handleDragLeave);
  });
});

// Add these new functions to your JavaScript file
function handleEditDragOver(event) {
  event.preventDefault();
  const dragArea = document.getElementById("editDragDropArea");
  dragArea.classList.add("bg-gray-100");
}

function handleEditDragLeave(event) {
  event.preventDefault();
  const dragArea = document.getElementById("editDragDropArea");
  dragArea.classList.remove("bg-gray-100");
}

function handleEditDrop(event) {
  event.preventDefault();
  const dragArea = document.getElementById("editDragDropArea");
  dragArea.classList.remove("bg-gray-100");

  const fileInput = document.getElementById("editFileInput");
  const files = event.dataTransfer.files;

  if (files.length > 0) {
    fileInput.files = files;
    updateEditFileNameDisplay(files[0].name);
  }
}

function updateEditFileNameDisplay(fileName) {
  const fileNameDisplay = document.getElementById("editFileNameDisplay");
  fileNameDisplay.textContent = `Selected File: ${fileName}`;
}

// Updated editRow function
function editRow(button) {
  const row = button.closest("tr");
  const fileNameCell = row.cells[2];
  const redirectLinkCell = row.cells[3];
  const currentFileName = fileNameCell.innerText.trim();
  const currentRedirectLink = redirectLinkCell.innerText.trim();

  // Show the Edit Modal
  const modal = document.getElementById("editMediaModal");
  modal.classList.remove("hidden");

  // Set up drag and drop area
  const dragArea = document.getElementById("editDragDropArea");
  dragArea.ondragover = handleEditDragOver;
  dragArea.ondragleave = handleEditDragLeave;
  dragArea.ondrop = handleEditDrop;

  // Add redirect link input if not exists
  const modalBody = modal.querySelector(".p-6");
  if (!document.getElementById("editRedirectLink")) {
    modalBody.insertAdjacentHTML(
      "beforeend",
      `
      <div class="mt-4">
        <label for="editRedirectLink" class="block text-lg font-medium text-gray-700"><strong>Redirect Link</strong></label>
        <input type="url" id="editRedirectLink" class="mt-2 block w-full border rounded p-2 border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500">
      </div>
    `
    );
  }

  // Set up existing values
  const fileInput = document.getElementById("editFileInput");
  const fileNameDisplay = document.getElementById("editFileNameDisplay");
  const redirectInput = document.getElementById("editRedirectLink");

  fileNameDisplay.textContent = `Current File: ${currentFileName}`;
  if (redirectInput && currentRedirectLink !== "No redirect link") {
    redirectInput.value = currentRedirectLink;
  }

  // Handle Save Button
  const saveButton = document.getElementById("saveEditedFile");
  saveButton.onclick = function () {
    const selectedFile = fileInput.files[0];
    const newRedirectLink = redirectInput ? redirectInput.value.trim() : "";

    // Update file name if new file selected
    if (selectedFile) {
      fileNameCell.innerText = selectedFile.name;
    }

    // Update redirect link
    redirectLinkCell.innerText = newRedirectLink || "No redirect link";

    closeEditModal();
    alert("Advertisement updated successfully!");
  };
}

// for close and open the modal of section 1,2,3
function openModal(id) {
  document.getElementById(id).classList.remove('hidden');
}
function closeModal(id) {
  document.getElementById(id).classList.add('hidden');
}    
