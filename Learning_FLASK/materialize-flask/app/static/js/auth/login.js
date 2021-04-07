const loginForm = document.getElementById("login-form");
const emailInput = document.getElementById("login-email-input");
const passwordInput = document.getElementById("login-password-input");
const submitButton = document.getElementById("login-submit-button");

loginForm.addEventListener("submit", (e) => {
  e.preventDefault();

  let entry = {
    email: emailInput.value,
    password: passwordInput.value,
  };

  postData(e, entry);
});

async function postData(e, entry) {
  fetch(`${window.origin}/auth/login`, {
    method: "POST",
    credentials: "same-origin",
    body: JSON.stringify(entry),
    cache: "no-cache",
    headers: new Headers({
      "Content-Type": "application/json",
      "X-CSRF-TOKEN": e.target.csrf_token.value,
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
}
