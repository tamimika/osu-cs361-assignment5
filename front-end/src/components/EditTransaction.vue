<template>
  <div class="container">
    <h1>Edit Transaction</h1>
    <form @submit.prevent="submitForm">
      <div>
        <label for="date">Date</label>
        <input type="date" id="date" v-model="transaction.date">
      </div>
      <div>
        <label for="cost">Cost</label>
        <input type="text" id="cost" v-model="transaction.cost">
      </div>
      <div>
        <label for="item">Item</label>
        <input type="text" id="item" v-model="transaction.item">
      </div>
      <div>
        <label for="vendor">Vendor</label>
        <input type="text" id="vendor" v-model="transaction.vendor">
      </div>
      <div>
        <label for="category">Category</label>
        <input type="text" id="category" v-model="transaction.category">
      </div>
      <button type="submit">Update</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      transaction: {
        date: '',
        cost: '',
        item: '',
        vendor: '',
        category: '',
      }
    };
  },
  methods: {
    async submitForm() {
      // Call the editTransaction function when the form is submitted
      await this.editTransaction()
    },
    async editTransaction() {
      // Format date into 'YYYY-MM-DD' format
      let dateObj = new Date(this.transaction.date);
      let year = dateObj.getFullYear();
      let month = ('0' + (dateObj.getMonth() + 1)).slice(-2);
      let date = ('0' + dateObj.getDate()).slice(-2);
      this.transaction.date = `${year}-${month}-${date}`;

      await axios.put(`http://127.0.0.1:5555/transactions/${this.transaction.id}`, this.transaction)
      this.$router.push('/')
    },
    fetchTransaction() {
      axios.get(`http://127.0.0.1:5555/transactions/${this.$route.params.id}`)
        .then(response => {
          this.transaction = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
  },
  beforeRouteEnter(to, from, next) {
    axios.get(`http://127.0.0.1:5555/transactions/${to.params.id}`)
      .then(response => {
        next(vm => {
          vm.transaction = response.data;
        });
      })
      .catch(error => {
        console.error(error);
        next(false);
      });
  },
  beforeRouteUpdate(to, from, next) {
    this.fetchTransaction();
    next();
  },
  mounted() {
    this.fetchTransaction();
  },
};
</script>

