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
  link.className = "secondary-content";
  link.innerHTML = '<i class="material-icons">clear</i>';
  li.appendChild(link);

  // Append li to ul
  taskList.appendChild(li);

  // clear input
  taskInput.value = "";

  console.log("Submit!");
  e.preventDefault();
}
