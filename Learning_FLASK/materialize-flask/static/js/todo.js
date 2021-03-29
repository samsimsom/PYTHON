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
  clearBtn.addEventListener("click", clearTasks);
  filterInput.addEventListener("keyup", filterTasks);
}

// Get Tasks from Local Storage
function getTasks() {
  let tasks;
  if (localStorage.getItem("tasks") === null) {
    tasks = [];
  } else {
    tasks = JSON.parse(localStorage.getItem("tasks"));
  }

  tasks.forEach(function (task) {
    // create list element
    let li = document.createElement("li");
    li.className = "collection-item";
    li.appendChild(document.createTextNode(task));

    // create new close link
    let link = document.createElement("a");
    link.className = "delete-item secondary-content";
    link.innerHTML = '<i class="material-icons">clear</i>';
    li.appendChild(link);

    // Append li to ul
    taskList.appendChild(li);
  });
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

  // Store in LocalStorage
  storeTaskInLocalStorage(taskInput.value);

  // clear input
  taskInput.value = "";

  // fetch('/add_todo').then(res => console.log(res));

  e.preventDefault();
}

// Remove Task
function removeTask(e) {
  if (e.target.parentElement.classList.contains("delete-item")) {
    if (confirm("Are you sure?")) {
      e.target.parentElement.parentElement.remove();

      // Remove from Local Storage
      removeTaskFromLocalStorage(e.target.parentElement.parentElement);
    }
  }
}

// Remove from Local Storage
function removeTaskFromLocalStorage(taskItem) {
  let tasks;
  if (localStorage.getItem("tasks") === null) {
    tasks = [];
  } else {
    tasks = JSON.parse(localStorage.getItem("tasks"));
  }

  tasks.forEach(function (task, index) {
    //FIXME: clear x butonundan gelen textContent
    // bunu temizlemenin yolunu bul.
    if (taskItem.textContent === task + "clear") {
      tasks.splice(index, 1);
    }
  });

  localStorage.setItem("tasks", JSON.stringify(tasks));
}

// Clear Tasks
function clearTasks() {
  while (taskList.firstChild) {
    taskList.removeChild(taskList.firstChild);
  }

  clearTasksFromLocalStorage();
}

// Clear Tasks From Local Storage
function clearTasksFromLocalStorage() {
  localStorage.clear();
}

// Filter Tasks
function filterTasks(e) {
  let text = e.target.value.toLowerCase();
  document.querySelectorAll(".collection-item").forEach(function (task) {
    let item = task.firstChild.textContent;
    if (item.toLowerCase().indexOf(text) != -1) {
      task.style.display = "block";
    } else {
      task.style.display = "none";
    }
  });
}

// Store in Local Storage
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
