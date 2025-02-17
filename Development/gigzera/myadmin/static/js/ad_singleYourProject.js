// Function to toggle the visibility of the progress edit form and enable/disable the status dropdown
function toggleProgressEdit() {
  const progressEditForm = document.getElementById("progressEditForm");
  const statusDropdown = document.getElementById("projectStatus");

  // Toggle the 'hidden' class for the edit form
  if (progressEditForm.classList.contains("hidden")) {
    progressEditForm.classList.remove("hidden"); // Show the edit form
    statusDropdown.disabled = false; // Enable the status dropdown
  } else {
    progressEditForm.classList.add("hidden"); // Hide the edit form
    statusDropdown.disabled = true; // Disable the status dropdown
  }
}

// Function to update the progress bar and reset the UI
function updateProgress() {
  const newProgress = document.getElementById("newProgress").value;
  const progressFill = document.getElementById("progressFill");
  const progressPercentage = document.getElementById("progressPercentage");
  const lastUpdatedBy = document.getElementById("lastUpdatedBy");
  const lastUpdatedTime = document.getElementById("lastUpdatedTime");
  const statusDropdown = document.getElementById("projectStatus");

  // Validate and update the progress
  if (newProgress >= 0 && newProgress <= 100) {
    progressFill.style.width = `${newProgress}%`; // Update progress bar width
    progressPercentage.textContent = `${newProgress}%`; // Update percentage
    lastUpdatedBy.textContent = "Current User"; // Update the user
    lastUpdatedTime.textContent = "just now"; // Update the timestamp

    // Hide the edit form and disable the status dropdown
    toggleProgressEdit();
  } else {
    alert("Please enter a value between 0 and 100.");
  }
}

// javascript for message box
function sendMessage() {
  const input = document.getElementById("messageInput");
  const container = document.getElementById("messagesContainer");

  if (input.value.trim()) {
    const messageDiv = document.createElement("div");
    messageDiv.className = "message sent";
    messageDiv.innerHTML = `  
        <img
              src="  https://cdn.yellowmessenger.com/cMvNTJMdqlfz1734610513305.jpeg"
              alt="User Avatar"
              class="user-avatar"
            /> 
            <div class="message-content">
                <p>${input.value}</p>  
                <span class="message-time">just now</span>  
            </div>
        `;
    container.appendChild(messageDiv);
    input.value = "";
    container.scrollTop = container.scrollHeight;
  }
}

// JavaScript for Timeline and Finance Sections
// Toggle Edit for Timeline Section
function toggleTimelineEdit() {
  const startDate = document.getElementById("startDate");
  const endDate = document.getElementById("endDate");

  // Toggle disabled state
  const isDisabled = startDate.disabled;
  startDate.disabled = !isDisabled;
  endDate.disabled = !isDisabled;

  // Provide feedback when exiting edit mode
  if (isDisabled === false) {
    if (new Date(startDate.value) > new Date(endDate.value)) {
      console.error("Start date cannot be later than the end date.");
      startDate.disabled = true;
      endDate.disabled = true;
    } else {
      console.log(
        `Timeline updated successfully: ${startDate.value} to ${endDate.value}`
      );
    }
  }
}

// Function to update Finance details
// Toggle Finance Edit Mode
function toggleFinanceEdit() {
  const financeInputs = document.querySelectorAll(
    ".finance .edit-table input, .finance .edit-table select, .milestone-btn"
  );
  const deleteIcons = document.querySelectorAll(".delete-icon"); // Select all delete icons

  // Check current state of inputs
  const isEditing = !financeInputs[0].disabled;

  // Update total costing dynamically before exiting edit mode
  if (isEditing) {
    updateFinance();
  }

  // Toggle disabled state for inputs
  financeInputs.forEach((input) => {
    input.disabled = isEditing;
  });
  // Toggle delete icon functionality (disable it when in edit mode)
  deleteIcons.forEach((icon) => {
    if (isEditing) {
      icon.style.pointerEvents = "none"; // Disable delete icon click in Edit mode
      icon.style.opacity = "0.5"; // Dimmed when in edit mode
    } else {
      icon.style.pointerEvents = "auto"; // Enable delete icon click outside of edit mode
      icon.style.opacity = "1"; // Full opacity when not in edit mode
    }
  });
}

// Update Total Cost Calculation dynamically when user enters values
function updateFinance() {
  const laborCost = parseFloat(document.getElementById("laborCost").value || 0);
  const consultingCharges = parseFloat(
    document.getElementById("consultingCharges").value || 0
  );

  // Calculate Total Costing
  const totalCosting = laborCost + consultingCharges;
  document.getElementById(
    "totalCosting"
  ).textContent = `$${totalCosting.toFixed(2)}`;
}

// Automatically update total cost when user changes values
document.getElementById("laborCost").addEventListener("input", updateFinance);
document
  .getElementById("consultingCharges")
  .addEventListener("input", updateFinance);

// Function to add a new milestone row with input fields
function addMilestoneRow() {
  const milestoneTable = document.getElementById("milestoneTable");

  // Create a new row
  const newRow = document.createElement("tr");

  // Create date input field
  const dateCell = document.createElement("td");
  const dateInput = document.createElement("input");
  dateInput.type = "date";
  dateInput.disabled = false; // Enable it for editing
  dateCell.appendChild(dateInput);

  // Create amount input field
  const amountCell = document.createElement("td");
  const amountInputWrapper = document.createElement("div");
  amountInputWrapper.classList.add("input-wrapper");
  const dollarSign = document.createElement("span");
  dollarSign.classList.add("dollar-sign");
  dollarSign.textContent = "$";
  const amountInput = document.createElement("input");
  amountInput.type = "number";
  amountInput.placeholder = "Amount";
  amountInput.disabled = false; // Enable it for editing
  amountInputWrapper.appendChild(dollarSign);
  amountInputWrapper.appendChild(amountInput);
  amountCell.appendChild(amountInputWrapper);

  // Create status select field
  const statusCell = document.createElement("td");
  const statusSelect = document.createElement("select");
  const optionPending = document.createElement("option");
  optionPending.value = "Pending";
  optionPending.textContent = "Pending";
  const optionCompleted = document.createElement("option");
  optionCompleted.value = "Completed";
  optionCompleted.textContent = "Completed";
  statusSelect.appendChild(optionPending);
  statusSelect.appendChild(optionCompleted);
  statusCell.appendChild(statusSelect);

  // Append the created cells to the new row
  newRow.appendChild(dateCell);
  newRow.appendChild(amountCell);
  newRow.appendChild(statusCell);

  // Append the new row to the table
  milestoneTable.appendChild(newRow);
}

// Attach an event listener to the "Add Milestones" button
document
  .getElementById("addMilestoneBtn")
  .addEventListener("click", addMilestoneRow);

// java script for modal
function openChatModal() {
  document.getElementById("chatModal").classList.remove("hidden");
}

// Close the message modal
function closeChatModal() {
  document.getElementById("chatModal").classList.add("hidden");
}

// Send a new message and display it in the message area
function sendNewMessage() {
  const input = document.getElementById("newMessageInput");
  const container = document.getElementById("messageArea");

  if (input.value.trim()) {
    const messageDiv = document.createElement("div");
    messageDiv.className = "message-box outgoing mb-3";
    messageDiv.innerHTML = `   
      <img src="https://cdn.yellowmessenger.com/cMvNTJMdqlfz1734610513305.jpeg" alt="User Avatar" class="avatar-img">
          <div class="message-content-box">
              <p>${input.value}</p>  
              <span class="time-stamp">just now</span>  
          </div>
      `;
    container.appendChild(messageDiv);
    input.value = "";
    container.scrollTop = container.scrollHeight;
  }
}

// Function to add a new milestone row with input fields
function addMilestoneRow() {
  const milestoneTable = document.getElementById("milestoneTable");

  // Create a new row
  const newRow = document.createElement("tr");

  // Create date input field
  const dateCell = document.createElement("td");
  const dateInput = document.createElement("input");
  dateInput.type = "date";
  dateInput.disabled = false; // Enable it for editing
  dateCell.appendChild(dateInput);

  // Create amount input field
  const amountCell = document.createElement("td");
  const amountInputWrapper = document.createElement("div");
  amountInputWrapper.classList.add("input-wrapper");
  const dollarSign = document.createElement("span");
  dollarSign.classList.add("dollar-sign");
  dollarSign.textContent = "$";
  const amountInput = document.createElement("input");
  amountInput.type = "number";
  amountInput.placeholder = "Amount";
  amountInput.disabled = false; // Enable it for editing
  amountInputWrapper.appendChild(dollarSign);
  amountInputWrapper.appendChild(amountInput);
  amountCell.appendChild(amountInputWrapper);

  // Create status select field
  const statusCell = document.createElement("td");
  const statusSelect = document.createElement("select");
  const optionPending = document.createElement("option");
  optionPending.value = "Pending";
  optionPending.textContent = "Pending";
  const optionCompleted = document.createElement("option");
  optionCompleted.value = "Completed";
  optionCompleted.textContent = "Completed";
  statusSelect.appendChild(optionPending);
  statusSelect.appendChild(optionCompleted);
  statusCell.appendChild(statusSelect);

  // Create delete icon
  const deleteCell = document.createElement("td");
  const deleteIcon = document.createElement("i");
  deleteIcon.classList.add("fa", "fa-trash", "delete-icon");
  deleteIcon.style.cursor = "pointer";
  deleteIcon.onclick = function () {
    // Delete the row when the delete icon is clicked
    milestoneTable.removeChild(newRow);
  };
  deleteCell.appendChild(deleteIcon);

  // Append the created cells to the new row
  newRow.appendChild(dateCell);
  newRow.appendChild(amountCell);
  newRow.appendChild(statusCell);
  newRow.appendChild(deleteCell);

  // Append the new row to the table
  milestoneTable.appendChild(newRow);
}

// Add the delete icon to pre-existing rows as well
document.querySelectorAll("#milestoneTable tr").forEach((row) => {
  const deleteCell = document.createElement("td");
  const deleteIcon = document.createElement("i");
  deleteIcon.classList.add("fa", "fa-trash", "delete-icon");
  deleteIcon.style.cursor = "pointer";
  deleteIcon.onclick = function () {
    // Delete the row when the delete icon is clicked
    row.parentElement.removeChild(row);
  };
  deleteCell.appendChild(deleteIcon);
  row.appendChild(deleteCell);
});
