// Define UI Vars
let form = document.querySelector("#task-form");
let taskInput = document.querySelector("#task-input");
let taskList = document.querySelector("#collection-list");
let clearBtn = document.querySelector("#clear-tasks-btn");
let filterInput = document.querySelector("#filter-input");

// Load all event listeners
loadEventListeners();

function loadEventListeners() {
  // DOM Load Event
  document.addEventListener("DOMContentLoaded", getTasks);

  form.addEventListener("submit", addTask);
  taskList.addEventListener("click", removeTask);
  filterInput.addEventListener("keyup", filterTasks);
  clearBtn.addEventListener("click", clearTasks);
}

// Create Task Element
function createTaskElement(task) {
  // Create list element
  let li = document.createElement("li");
  li.className = "list-group-item";
  li.id = Date.now().toString();
  li.innerHTML = `
    <div class="d-flex flex-row" id="collection-element">
      <div class="d-flex flex-fill">${task}</div>
      <div class="d-flex">
        <button 
          type="button" 
          class="delete-task btn-close" 
          aria-label="Close" 
          id=${Date.now().toString()}>
          </button>
      </div>
    </div>
    `;

  // Append li to ul
  taskList.appendChild(li);
}

// Add Task
function addTask(e) {
  // Create Task Element
  createTaskElement(taskInput.value);
  // Store in LocalStorage
  storeTaskInLocalStorage(taskInput.value);
  // Clear Task Input
  taskInput.value = "";
  // From Default
  e.preventDefault();
}

// Remove Task
function removeTask(e) {
  let taskElement = document.getElementById(e.target.id);
  if (e.target.classList.contains("delete-task")) {
    if (confirm("Are you sure?")) {
      if (e.target.id === taskElement.id) {
        taskElement.remove();
        // Remove From LocalStorage
        removeTaskFromLocalStorage(taskElement);
      }
    }
  }
}

// Filter Tasks
function filterTasks(e) {
  let text = e.target.value.toLowerCase();
  document.querySelectorAll("#collection-element").forEach(function (task) {
    // console.log(task.parentElement);
    let item = task.textContent;
    if (item.toLowerCase().indexOf(text) != -1) {
      task.parentElement.style.display = "block";
    } else {
      task.parentElement.style.display = "none";
    }
  });
}

// Clear Tasks
function clearTasks() {
  if (confirm("Are you sure?")) {
    while (taskList.firstChild) {
      taskList.removeChild(taskList.firstChild);
    }
    clearTasksFromLocalStorage();
  }
}

// -----------------------------------------------------------------------------
// Get Tasks From LocalStorage
function getTasks(params) {
  let tasks;
  if (localStorage.getItem("tasks") === null) {
    tasks = [];
  } else {
    tasks = JSON.parse(localStorage.getItem("tasks"));
  }

  tasks.forEach(function (task) {
    createTaskElement(task);
  });
}

// Store in LocalStorage
function storeTaskInLocalStorage(task) {
  let tasks;
  if (localStorage.getItem("tasks") === null) {
    tasks = [];
  } else {
    tasks = JSON.parse(localStorage.getItem("tasks"));
  }

  tasks.push(task);
  localStorage.setItem("tasks", JSON.stringify(tasks));
}

// Romove From Local Storage
function removeTaskFromLocalStorage(taskItem) {
  let tasks;
  if (localStorage.getItem("tasks") === null) {
    tasks = [];
  } else {
    tasks = JSON.parse(localStorage.getItem("tasks"));
  }

  tasks.forEach(function (task, index) {
    if (taskItem.textContent.trim() === task) {
      tasks.splice(index, 1);
      console.log(true);
    }
  });

  localStorage.setItem("tasks", JSON.stringify(tasks));
}

// Remove All From Local Storage
function clearTasksFromLocalStorage() {
  localStorage.clear();
}
