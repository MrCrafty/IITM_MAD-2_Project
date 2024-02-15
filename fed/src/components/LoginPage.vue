<script setup>
async function handleFormSubmit() {
  var username = document.getElementById('username').value
  var password = document.getElementById('password').value

  await fetch('http://localhost:8000/auth/login', {
    headers: {
      'content-type': 'application/json'
    },
    method: 'POST',
    body: JSON.stringify({ username: username, password: password })
  }).then(
    () => (window.location.href = '/'),
    () => alert('something went wrong')
  )
}
</script>
<template>
  <div class="component-wrapper">
    <div class="container">
      <div class="row">
        <div
          class="login-wrapper col-6 d-flex flex-column justify-content-center align-items-center border-end border-light shadow-lg"
        >
          <div class="text-black w-100">
            <div class="w-75 border border-1 border-white p-5 rounded-4">
              <h1 class="fs-1 text-light text-center mb-4">Login</h1>
              <form class="d-flex flex-column gap-5" @submit.prevent="handleFormSubmit">
                <input
                  type="text"
                  name="username"
                  id="username"
                  class="bg-transparent border-0 border-bottom border-primary username-input text-white"
                  placeholder="Enter Username"
                />
                <input
                  type="password"
                  name="password"
                  id="password"
                  class="bg-transparent border-0 border-bottom border-primary username-input text-white"
                  placeholder="Enter Password"
                />
                <button class="btn btn-primary fs-4">Login</button>
              </form>
            </div>
          </div>
        </div>
        <div class="login-img-wrapper col-6 d-flex justify-content-center">
          <img src="../assets/login.png" alt="" class="w-75" />
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped>
.component-wrapper {
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  background-color: rgb(20, 20, 20);
}
input {
  padding: 1rem;
}
input::placeholder {
  font-size: 2rem;
}
.username-input {
  outline: none;
  font-size: 1.5rem;
  font-weight: 500;
}
</style>
