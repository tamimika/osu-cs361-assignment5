<template>
  <div>
    <h1>Data from JSON API</h1>
    <ul>
      <li v-for="(item, index) in items" :key="index">{{ item }}</li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      items: []
    }
  },
  async created() {
    const response = await axios.get('http://127.0.0.1:5555/transactions')
    this.items = response.data
  }
}
</script>
