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
         <option>Requirement Gathering</option>
                  <option>Designing</option>
                  <option>Development</option>
                  <option>Testing</option>
                  <option>UAT</option>
                  <option>Completed</option>
      </select>
    </div>
    <div class="task-comment">
     <button onclick="openChatModal()" class="comment-button" disabled>
      Add Comment
      </button>          
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
  const commentButton = task.querySelector(".comment-button");

  editIcon.addEventListener("click", () => {
    if (editIcon.classList.contains("editing")) {
      // Save and reset after editing
      title.contentEditable = "false";
      commentButton.disabled = true;
      editIcon.classList.remove("editing");
      editIcon.style.color = "#007bff"; // Reset icon color
    } else {
      // Enable editing
      title.contentEditable = "true";
      commentButton.disabled = false;
      title.focus();
      editIcon.classList.add("editing");
      editIcon.style.color = "#0056b3"; // Indicate editing mode
    }
  });
  // Open comment modal and set task reference
  commentButton.addEventListener("click", () => {
    if (!commentButton.disabled) {
      openChatModal(task);
    }
  });
}

// Initialize edit functionality for existing tasks
document
  .querySelectorAll(".task")
  .forEach((task) => addEditFunctionality(task));

// Open the message modal when clicking 'Add Comment'
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
