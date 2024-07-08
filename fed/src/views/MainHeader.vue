<script setup>
import AdminHeader from '@/components/AdminHeader.vue'
import UserHeader from '@/components/UserHeader.vue'
import AnonHeader from '@/components/AnonHeader.vue'
import axios from 'axios'
</script>
<script>
export default {
  data() {
    return {
      user: {}
    }
  },
  async created() {
    await axios
      .get('http://localhost:8000/user')
      .then((data) => (this.user = JSON.parse(data.data)))
    console.log('data', this.user)
  }
}
</script>
<template>
  <div class="bg-dark fixed-top fs-4">
    <div class="container">
      <div v-if="user?.status == 'false'"><AnonHeader /></div>
      <div v-else-if="user?.status == 'true' && user?.message?.role == 'admin'">
        <AdminHeader />
      </div>
      <div v-else><UserHeader :user="{ name: user?.value?.message?.username }" /></div>
    </div>
  </div>
</template>
