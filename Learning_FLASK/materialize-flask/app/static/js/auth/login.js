const loginForm = document.getElementById("login-form");
const emailInput = document.getElementById("login-email-input");
const passwordInput = document.getElementById("login-password-input");
const submitButton = document.getElementById("login-submit-button");

loginForm.addEventListener("submit", loginFormSubmited);

function loginFormSubmited(e) {
  let entry = {
    name: emailInput.value,
    message: passwordInput.value,
  };

  fetch(`${window.origin}/auth/login`, {
    method: "POST",
    credentials: "include",
    body: JSON.stringify(entry),
    cache: "no-cache",
    headers: new Headers({
      "content-type": "application/json",
    }),
  })
    .then(function (response) {
      if (response.status !== 200) {
        console.log(
          `Looks like there was a problem. Status code: ${response.status}`
        );
        return;
      }
      response.json().then(function (data) {
        console.log(data);
      });
    })
    .catch(function (error) {
      console.log("Fetch error: " + error);
    });
  e.preventDefault();
}

// function loginFormSubmited(e) {
//   postData(`${window.origin}/auth/login`, {
//     email: emailInput.value,
//     password: passwordInput.value,
//   }).then((data) => {
//     console.log(data);
//     loginForm.reset();
//   });

//   e.preventDefault();
// }

// async function postData(url = "", data = {}) {
//   const response = await fetch(url, {
//     method: "POST",
//     mode: "cors",
//     cache: "no-cache",
//     credentials: "same-origin",
//     headers: {
//       "Content-Type": "application/json",
//     },
//     redirect: "follow",
//     referrerPolicy: "no-referrer",
//     body: JSON.stringify(data),
//   });
//   return response.json();
// }
