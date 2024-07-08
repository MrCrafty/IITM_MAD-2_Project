<template>
  <div v-for="(item, index) in section" :key="index" class="container">
    <div class="d-flex">
      <div class="border-black border rounded-2 p-5 d-flex flex-column">
        <h1>{{ item.section_name }}</h1>
        <p>{{ item.description }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    section: Array
  }
}
</script>
