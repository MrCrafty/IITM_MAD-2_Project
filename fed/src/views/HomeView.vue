<script setup>
import LoginPage from '@/components/LoginPage.vue'
import axios from 'axios'
</script>
<script>
export default {
  data() {
    return {
      IsLoggedIn: ''
    }
  },
  async mounted() {
    await axios
      .get('http://localhost:8000/user')
      .then((data) => (this.IsLoggedIn = JSON.parse(data?.data)?.status))
  }
}
</script>

<template>
  <div v-if="IsLoggedIn == 'true'">
    <h1>Logged In</h1>
  </div>
  <div v-else>
    <LoginPage />
  </div>
</template>
