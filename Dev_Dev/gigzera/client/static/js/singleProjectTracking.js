// javascript for progress
// Function to toggle the visibility of the progress edit form
function toggleProgressEdit() {
  const progressEditForm = document.getElementById("progressEditForm");

  // Toggle the 'hidden' class
  if (progressEditForm.classList.contains("hidden")) {
    progressEditForm.classList.remove("hidden"); // Show the edit form
  } else {
    progressEditForm.classList.add("hidden"); // Hide the edit form
  }
}

// Function to update the progress bar and reset the UI
function updateProgress() {
  const newProgress = document.getElementById("newProgress").value;
  const progressFill = document.getElementById("progressFill");
  const progressPercentage = document.getElementById("progressPercentage");
  const lastUpdatedBy = document.getElementById("lastUpdatedBy");
  const lastUpdatedTime = document.getElementById("lastUpdatedTime");

  // Validate and update the progress
  if (newProgress >= 0 && newProgress <= 100) {
    progressFill.style.width = `${newProgress}%`; // Update progress bar width
    progressPercentage.textContent = `${newProgress}%`; // Update percentage
    lastUpdatedBy.textContent = "Current User"; // Update the user
    lastUpdatedTime.textContent = "just now"; // Update the timestamp

    // Hide the edit form
    toggleProgressEdit();
  } else {
    alert("Please enter a value between 0 and 100.");
  }
}
// javascript for task box
// JavaScript to add new task when button is clicked
document.getElementById("addTaskBtn").addEventListener("click", () => {
  const taskList = document.querySelector(".task-list");

  // Create new task div
  const newTask = document.createElement("div");
  newTask.classList.add("task");
  newTask.innerHTML = `
    <div class="task-row">
      <input type="checkbox" class="task-checkbox">
      <label class="task-title">New Task</label>
      <i class="fa-solid fa-pen-to-square edit-icon"></i>
      <select>
        <option>In Progress</option>
        <option>Completed</option>
        <option>Pending</option>
      </select>
    </div>
    <div class="task-comment">
      <textarea class="comment-box" placeholder="Add a comment..." disabled></textarea>
    </div>
  `;

  taskList.appendChild(newTask);
  addEditFunctionality(newTask);
});

document.getElementById("deleteSelectedBtn").addEventListener("click", () => {
  const tasks = document.querySelectorAll(".task");
  tasks.forEach((task) => {
    const checkbox = task.querySelector(".task-checkbox");
    if (checkbox.checked) {
      task.remove();
    }
  });
});

function addEditFunctionality(task) {
  const editIcon = task.querySelector(".edit-icon");
  const title = task.querySelector(".task-title");
  const commentBox = task.querySelector(".comment-box");

  editIcon.addEventListener("click", () => {
    if (editIcon.classList.contains("editing")) {
      // Save and reset after editing
      title.contentEditable = "false";
      commentBox.disabled = true;
      editIcon.classList.remove("editing");
      editIcon.style.color = "#007bff"; // Reset icon color
    } else {
      // Enable editing
      title.contentEditable = "true";
      commentBox.disabled = false;
      title.focus();
      editIcon.classList.add("editing");
      editIcon.style.color = "#0056b3"; // Indicate editing mode
    }
  });
}

// Initialize edit functionality for existing tasks
document
  .querySelectorAll(".task")
  .forEach((task) => addEditFunctionality(task));

// javascript for message box
function sendMessage() {
  const input = document.getElementById("messageInput");
  const container = document.getElementById("messagesContainer");

  if (input.value.trim()) {
    const messageDiv = document.createElement("div");
    messageDiv.className = "message sent";
    messageDiv.innerHTML = `   
            <div class="message-content">
                <p>${input.value}</p>  
                <span class="message-time">just now</span>  
            </div>
            <img src="/api/placeholder/32/32" alt="User Avatar" class="user-avatar">
        `;
    container.appendChild(messageDiv);
    input.value = "";
    container.scrollTop = container.scrollHeight;
  }
}
