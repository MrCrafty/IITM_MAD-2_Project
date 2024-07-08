<template>
  <div class="component-wrapper">
    <SectionList :section="this.section" />
  </div>
</template>
<script>
import axios from 'axios'
import SectionList from './SectionList.vue'
export default {
  name: 'AdminDash',
  data() {
    return {
      section: []
    }
  },
  methods: {
    getSection() {
      axios.get('http://localhost:8000/section').then((response) => {
        console.log(response.data)
        this.section = response.data
      })
    }
  },
  created() {
    this.getSection()
  },
  components: { SectionList }
}
</script>
<style scoped></style>
