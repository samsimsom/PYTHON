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
  document.addEventListener("DOMContentLoaded", get_task_from_mongo);

  form.addEventListener("submit", addTask);
  taskList.addEventListener("click", removeTask);
  filterInput.addEventListener("keyup", filterTasks);
  // clearBtn.addEventListener("click", clearTasks);
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
  // store task in database
  console.log(store_task_in_mongo(taskInput.value));


  createTaskElement(taskInput.value);
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



// -----------------------------------------------------------------------------

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
// function clearTasksFromLocalStorage() {
//   localStorage.clear();
// }

// -----------------------------------------------------------------------------
// Clear Tasks
function clear_tasks_from_html() {
  while (taskList.firstChild) {
    taskList.removeChild(taskList.firstChild);
  }
}

// Get Task From Mongo
function get_task_from_mongo() {
  fetch(`${window.origin}/get_todo`)
    .then((responce) => responce.json())
    .then((tasks) => {
      tasks.forEach(function (task) {
        createTaskElement(task['task']);
      });
    });
}

// store in mongo
function store_task_in_mongo(task) {
  fetch(`${window.origin}/add_todo`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      task: task,
    }),
  }).then((res) => {
    console.log(res.ok);
  });
}

/*
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
  storeTaskInMongo(taskInput.value);

  // clear input
  taskInput.value = "";

  e.preventDefault();
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

// store in mongo
function storeTaskInMongo(task) {
  fetch(`${window.origin}/add_todo`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      task: task
    })
  }).then(res => console.log(res));

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

*/
