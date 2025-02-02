//  Model js for add certificate
document
  .getElementById("file-input-cert")
  .addEventListener("change", function (event) {
    const file = event.target.files[0];
    if (file) {
      document.getElementById("uploaded-file-cert").classList.remove("hidden");
      document.getElementById("file-name-cert").textContent = file.name;
      document.getElementById("file-size-cert").textContent =
        (file.size / 1024).toFixed(2) + " KB";
    }
  });

function removeFile() {
  document.getElementById("uploaded-file-cert").classList.add("hidden");
  document.getElementById("file-input-cert").value = "";
}

function openModal() {
  document.getElementById("addCertificateModal").classList.remove("hidden");
}

function closeModal() {
  document.getElementById("addCertificateModal").classList.add("hidden");
}

// Model js for Work History
function openWorkHistoryModal() {
  document.getElementById("workHistoryModal").classList.remove("hidden");
}

function closeWorkHistoryModal() {
  document.getElementById("workHistoryModal").classList.add("hidden");
}

// Automatically disable "Worked Till" if "Currently Working" is checked
document
  .getElementById("currentlyWorking")
  .addEventListener("change", function () {
    const workedTill = document.getElementById("workedTill");
    workedTill.disabled = this.checked;
    if (this.checked) {
      workedTill.value = "";
    }
  });

//   Old profile js file code

// Certification Modal Elements
const fileInputcert = document.getElementById("file-input-cert");
const uploadedFiles = document.getElementById("uploaded-file-cert");
const fileNameSpan = document.getElementById("file-name-cert");
const fileSizeSpan = document.getElementById("file-size-cert");
const issueDateInput = document.getElementById("issue-date");
const expiryDateInput = document.getElementById("expiry-date");
const certificationNameInput = document.getElementById("certification-name");
const certificationIdInput = document.getElementById("certification-id");
const certificationUrlInput = document.getElementById("certification-url");
const saveButton = document.getElementById("save-button");

// Open and Close Modal Functions for Certification
function openCertificateModal() {
  document.getElementById("workHistoryModal").classList.remove("hidden");
}

function closeCertificateModal() {
  document.getElementById("workHistoryModal").classList.add("hidden");
}

// File Upload Handling
fileInputcert.addEventListener("change", (event) => {
  const file = event.target.files[0];
  if (file) {
    fileNameSpan.textContent = file.name;
    fileSizeSpan.textContent = (file.size / 1024).toFixed(2) + " KB";
    uploadedFiles.style.display = "flex";
  }
});

function removeFile() {
  fileInputcert.value = "";
  uploadedFiles.style.display = "none";
}

// Save Button Click for Certification Modal
saveButton.addEventListener("click", () => {
  if (!fileInputcert.files[0]) {
    alert("Please upload a file.");
    return;
  }
  if (!certificationNameInput.value) {
    alert("Please enter a certification name.");
    return;
  }
  if (!issueDateInput.value) {
    alert("Please select an issue date.");
    return;
  }

  const formData = {
    fileName: fileInputcert.files[0].name,
    fileSize: (fileInputcert.files[0].size / 1024).toFixed(2) + " KB",
    issueDate: issueDateInput.value,
    expiryDate: expiryDateInput.value,
    certificationName: certificationNameInput.value,
    certificationId: certificationIdInput.value,
    certificationUrl: certificationUrlInput.value,
  };

  console.log("Certification Data Saved:", formData);

  // Reset the form
  fileInputcert.value = "";
  uploadedFiles.style.display = "none";
  issueDateInput.value = "";
  expiryDateInput.value = "";
  certificationNameInput.value = "";
  certificationIdInput.value = "";
  certificationUrlInput.value = "";

  // Close the modal
  closeCertificateModal();
});

// Work History Modal Elements
const currentlyWorkingCheckbox = document.getElementById("currentlyWorking");
const workedTillField = document.getElementById("workedTill");
const saveWorkHistoryButton = document.getElementById("saveBtn");

// Open and Close Modal Functions for Work History
function openWorkHistoryModal() {
  document.getElementById("workHistoryModal").classList.remove("hidden");
}

function closeWorkHistoryModal() {
  document.getElementById("workHistoryModal").classList.add("hidden");
}

// Handle "Currently Working" Checkbox
currentlyWorkingCheckbox.addEventListener("change", function () {
  if (this.checked) {
    workedTillField.value = "";
    workedTillField.disabled = true;
    workedTillField.removeAttribute("required");
  } else {
    workedTillField.disabled = false;
    workedTillField.setAttribute("required", "true");
  }
});

// Save Button Click for Work History Modal
saveWorkHistoryButton.addEventListener("click", () => {
  const company = document.getElementById("company").value.trim();
  const title = document.getElementById("title").value.trim();
  const city = document.getElementById("city").value.trim();
  const country = document.getElementById("country").value.trim();
  const workedFrom = document.getElementById("workedFrom").value;
  const workedTill = document.getElementById("workedTill").value;
  const currentlyWorking = document.getElementById("currentlyWorking").checked;
  const description = document.getElementById("description").value.trim();

  if (!company || !title || !city || !country || !workedFrom) {
    alert("Please fill out all required fields.");
    return;
  }

  if (!currentlyWorking && !workedTill) {
    alert("Please specify the Worked Till date.");
    return;
  }

  const workHistory = {
    company,
    title,
    city,
    country,
    workedFrom,
    workedTill: currentlyWorking ? "Present" : workedTill,
    description,
  };

  console.log("Work History Saved:", workHistory);

  // Close the modal
  closeWorkHistoryModal();
});
