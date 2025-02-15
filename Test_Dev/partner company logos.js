// Function to edit the row
function editRow(button) {
  const row = button.closest("tr");
  const mediaLinkCell = row.cells[1];
  const currentMediaLink = mediaLinkCell.textContent.trim();

  // Save the row reference and current media link for later use
  editRowData = row;
  originalMediaLink = currentMediaLink;

  // Update the modal with the current file name
  const mediaUploadContainer = document.getElementById("editMediaUpload");
  mediaUploadContainer.innerHTML = `
        <p>File selected: <strong>${currentMediaLink}</strong></p>
        <p>Click to select a new file or drag-and-drop here.</p>
    `;

  // Show the edit modal
  openModaledit();
}

// Function to delete the row
function deleteRow(button) {
  const row = button.closest("tr");
  const tableBody = row.closest("tbody");

  if (confirm("Are you sure you want to delete this row?")) {
    row.remove();
    
    // Update serial numbers
    Array.from(tableBody.rows).forEach((row, index) => {
      row.cells[0].textContent = `${index + 1}.`;
    });
  }
}

// Function to save a new advertisement
function saveNewMediaLink() {
  if (!uploadedFile) {
    alert("Please upload a media file first.");
    return;
  }

  const tableBody = document.getElementById("adsTableBody");
  const serialNumber = tableBody.rows.length + 1;

  const newRow = document.createElement("tr");
  newRow.innerHTML = `
    <td>${serialNumber}.</td>
    <td>${uploadedFile.name}</td>
    <td>
      <button class="edit-button bg-yellow-500 text-black px-3.5 py-1 rounded-md hover:bg-yellow-600" onclick="editRow(this)">
        <i class="fas fa-edit mr-2"></i> Edit
      </button>
      <button class="delete-button bg-red-500 text-white px-3.5 py-1 rounded-md hover:bg-red-600" onclick="deleteRow(this)">
        <i class="fas fa-trash-alt mr-2"></i> Delete
      </button>
    </td>
  `;
  tableBody.appendChild(newRow);

  // Hide the modal
  closeModal();

  // Reset form
  document.getElementById("addMediaLinkForm").reset();
  document.getElementById("mediaUpload").innerHTML = `
    <p>Drag and drop your file here, or click to select a file.</p>
  `;
  uploadedFile = null;
}

// Save edited media link and update the row
function saveEditedMedia() {
  if (!uploadedFile && !originalMediaLink) {
    alert("Please upload a media file or keep the existing link.");
    return;
  }

  const mediaLinkCell = editRowData.cells[1];
  mediaLinkCell.textContent = uploadedFile ? uploadedFile.name : originalMediaLink;

  // Hide the modal
  closeModaledit();

  // Reset state
  uploadedFile = null;
  originalMediaLink = null;
}

// Modal functions
function openModal() {
  document.getElementById("createAdModal").classList.remove("hidden");
}

function closeModal() {
  document.getElementById("createAdModal").classList.add("hidden");
}

function openModaledit() {
  document.getElementById("editAdModal").classList.remove("hidden");
}

function closeModaledit() {
  document.getElementById("editAdModal").classList.add("hidden");
}

// File selection handling
function handleFileSelect(event) {
  uploadedFile = event.target.files[0];
  if (uploadedFile) {
    document.getElementById("mediaUpload").innerHTML = `
      <p>File selected: ${uploadedFile.name}</p>
      <p>Size: ${(uploadedFile.size / 1024 / 1024).toFixed(2)} MB</p>
    `;
  }
}

function handleFileSelectForEdit(event) {
  uploadedFile = event.target.files[0];
  if (uploadedFile) {
    document.getElementById("editMediaUpload").innerHTML = `
      <p>File selected: ${uploadedFile.name}</p>
      <p>Size: ${(uploadedFile.size / 1024 / 1024).toFixed(2)} MB</p>
    `;
  }
}
