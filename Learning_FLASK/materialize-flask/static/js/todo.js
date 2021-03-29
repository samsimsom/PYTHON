// Define UI Vars

let form = document.querySelector("#task-form");
let taskInput = document.querySelector("#task-input");
let taskList = document.querySelector("#collection-list");
let clearBtn = document.querySelector("#clear-tasks-btn");
let filterInput = document.querySelector("#filter-input");

// Load all event listeners
loadEventListeners();

function loadEventListeners() {
  form.addEventListener("submit", addTask);
  taskList.addEventListener("click", removeTask);
  clearBtn.addEventListener("click", clearTasks);
  filterInput.addEventListener("keyup", filterTasks);
}

// Add Task
function addTask(e) {
  if (taskInput.value === "") {
    alert("Add a Task");
    return;
  }

  // create list element
  let li = document.createElement("li");
  li.className = "collection-item";
  li.appendChild(document.createTextNode(taskInput.value));

  // create new close link
  let link = document.createElement("a");
  link.className = "delete-item secondary-content";
  link.innerHTML = '<i class="material-icons">clear</i>';
  li.appendChild(link);

  // Append li to ul
  taskList.appendChild(li);

  // clear input
  taskInput.value = "";

  console.log("Submit!");

  // fetch('/add_todo').then(res => console.log(res));

  e.preventDefault();
}

// Remove Task
function removeTask(e) {
  if (e.target.parentElement.classList.contains("delete-item")) {
    if (confirm("Are you sure?")) {
      e.target.parentElement.parentElement.remove();
    }
  }
}

// Clear Tasks
function clearTasks() {
  while (taskList.firstChild) {
    taskList.removeChild(taskList.firstChild);
  }
}

// Filter Tasks
function filterTasks(e) {
  let text = e.target.value.toLowerCase();
  document.querySelectorAll(".collection-item").forEach
  (function (task) {
    let item = task.firstChild.textContent;
    if (item.toLowerCase().indexOf(text) != -1) {
      task.style.display = "block";
    } else {
      task.style.display = "none";
    }
  });
}
