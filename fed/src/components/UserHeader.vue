<template>
  <nav class="navbar navbar-expand-lg">
    <a class="navbar-brand fs-1" href="#">Hello {{ user.name }}</a>
    <button
      class="navbar-toggler"
      type="button"
      data-toggle="collapse"
      data-target="#navbarNav"
      aria-controls="navbarNav"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link" href="#">My Books</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Books</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Stats</a>
        </li>
        <li class="nav-item">
          <button class="btn btn-danger">Sign Out</button>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {
  props: {
    user: { name: String }
  }
}
</script>
