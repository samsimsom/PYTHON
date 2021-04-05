const loginForm = document.getElementById("login-form");
const emailInput = document.getElementById("login-email-input");
const passwordInput = document.getElementById("login-password-input");
const submitButton = document.getElementById("login-submit-button");

loginForm.addEventListener("submit", loginFormSubmited);

function loginFormSubmited(e) {
  postData(`${window.origin}/auth/login-form-submit`, {
    email: emailInput.value,
    password: passwordInput.value,
  }).then((data) => {
    console.log(data);
    loginForm.reset();
  });

  e.preventDefault();
}

async function postData(url = "", data = {}) {
  const response = await fetch(url, {
    method: "POST",
    mode: "cors",
    cache: "no-cache",
    credentials: "same-origin",
    headers: {
      "Content-Type": "application/json",
    },
    redirect: "follow",
    referrerPolicy: "no-referrer",
    body: JSON.stringify(data),
  });
  return response.json();
}
