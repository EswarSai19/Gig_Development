document.addEventListener("DOMContentLoaded", function () {
  const modal = document.getElementById("addCertificateModal");
  const openModalBtn = document.getElementById("open-modal-btn");
  const cancelBtn = document.getElementById("cancel-btn");
  const saveBtn = document.getElementById("save-btn");

  // File Upload
  const fileInput = document.getElementById("file-input");
  const dropArea = document.getElementById("drop-area");
  const browseBtn = document.getElementById("browse-btn");
  const uploadedFile = document.getElementById("uploaded-file");
  const fileNameSpan = document.getElementById("file-name");
  const fileSizeSpan = document.getElementById("file-size");
  const removeFileBtn = document.getElementById("remove-file");

  // Open Modal
  openModalBtn.addEventListener("click", () => {
    modal.classList.remove("hidden");
  });

  // Close Modal
  cancelBtn.addEventListener("click", () => {
    modal.classList.add("hidden");
  });

  // Handle file selection
  browseBtn.addEventListener("click", () => fileInput.click());
  fileInput.addEventListener("change", handleFileUpload);

  dropArea.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropArea.classList.add("bg-gray-200");
  });

  dropArea.addEventListener("dragleave", () => {
    dropArea.classList.remove("bg-gray-200");
  });

  dropArea.addEventListener("drop", (e) => {
    e.preventDefault();
    dropArea.classList.remove("bg-gray-200");

    if (e.dataTransfer.files.length > 0) {
      fileInput.files = e.dataTransfer.files;
      handleFileUpload();
    }
  });

  function handleFileUpload() {
    const file = fileInput.files[0];
    if (file) {
      fileNameSpan.textContent = file.name;
      fileSizeSpan.textContent = `(${(file.size / 1024).toFixed(2)} KB)`;
      uploadedFile.classList.remove("hidden");
    }
  }

  removeFileBtn.addEventListener("click", () => {
    fileInput.value = "";
    uploadedFile.classList.add("hidden");
  });

  // Save Button Functionality (Validation Example)
  saveBtn.addEventListener("click", () => {
    const certName = document.getElementById("certification-name").value;
    const issueDate = document.getElementById("issue-date").value;

    if (!certName || !issueDate) {
      alert("Please fill in the required fields.");
      return;
    }

    alert("Certification details saved successfully!");
    modal.classList.add("hidden");
  });
});
