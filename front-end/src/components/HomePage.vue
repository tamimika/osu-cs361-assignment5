<template>
  <div class="p-6">
    <h1 class="text-3xl font-bold mb-4">Monthly Budget App</h1>

    <label for="salary" class="block text-xs font-medium text-gray-500 uppercase tracking-wider">Salary</label>
    <h1 @click="editingSalary = true" class="text-3xl font-bold dark:text-black h-16" v-if="!editingSalary">${{ salary }}</h1>
    <input v-else v-model="salary" @blur="updateSalary" />
    <div v-if="showPopup" class="popup">Salary updated!</div>

    <h5 class="text-xl font-bold dark:text-black">Transactions</h5>
    <button @click="addTransaction" class="px-4 py-2 bg-green-500 text-white">New Transaction</button>
    <table class="min-w-full divide-y divide-gray-200">
      <thead class="bg-gray-50">
        <tr>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
            Date
          </th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
            Cost
          </th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
            Item
          </th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
            Vendor
          </th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
            Category
          </th>
          <th scope="col" class="relative px-6 py-3">
            <span class="sr-only">Edit</span>
          </th>
        </tr>
      </thead>

      <tbody class="bg-white divide-y divide-gray-200">
        <tr v-for="transaction in transactions" :key="transaction.id">
          <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
            <input class="text-sm text-grey-500 p-2" v-if="editMode[transaction.id]" v-model="transaction.date" />
            <span v-else class="text-sm text-gray-500">{{ transaction.date }}</span>
          </td>
          <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
            <input class="text-sm text-grey-500 p-2" v-if="editMode[transaction.id]" v-model="transaction.cost" />
            <span v-else>{{ transaction.cost }}</span>
          </td>
          <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
            <input class="text-sm text-grey-500 p-2" v-if="editMode[transaction.id]" v-model="transaction.item" />
            <span v-else>{{ transaction.item }}</span>
          </td>
          <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
            <input class="text-sm text-grey-500 p-2" v-if="editMode[transaction.id]" v-model="transaction.vendor" />
            <span v-else>{{ transaction.vendor }}</span>
          </td>
          <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
            <input class="text-sm text-grey-500 p-2" v-if="editMode[transaction.id]" v-model="transaction.category" />
            <span v-else>{{ transaction.category}}</span>
          </td>
          <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
            <button v-if="editMode[transaction.id]" @click="saveTransaction(transaction.id)" class="px-4 py-2 bg-blue-500 text-white">Save</button>
            <button v-else @click="editTransaction(transaction.id)" class="px-4 py-2 bg-blue-500 text-white">Edit</button>
            <button @click="deleteTransaction(transaction.id)" class="px-4 py-2 bg-red-500 text-white">Delete</button>
            <!-- <button @click="console.log(transaction)">Debug</button> -->
          </td>
        </tr>
      </tbody>
    </table>

    <h5 class="text-xl font-bold dark:text-black">Upload Transactions</h5>

    <div class="flex items-center justify-center w-full">
      <label for="dropzone-file" class="flex flex-col items-center justify-center w-full h-32 rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-gray-300 dark:bg-gray-200 hover:bg-gray-100  dark:hover:border-gray-500 dark:hover:bg-gray-600">
        <div class="flex flex-col items-center justify-center pt-5 pb-6">
          <p class="mb-2 text-sm text-gray-500 dark:text-gray-400"><span class="font-semibold">Click to upload transactions</span> or drag and drop</p>
        </div>
        <input id="dropzone-file" type="file" class="hidden" />
      </label>
    </div>

  </div>
</template>

<script>
  import axios from 'axios';

  export default {
    data() {
      return {
        salary: 60000,
        editingSalary: false,
        showPopup: false,
        transactions: [],
        transactionIdCounter: 0,  // Keep track of unique id for transactions
        editMode: {},  // Track which transactions are being edited
      };
    },
    created() {
      const userId = 1;  // Replace with the actual user_id.
      axios.get(`http://127.0.0.1:5555/salary/${userId}`)
      .then(response => {
          // The salary data is in response.data if the request was successful.
          this.salary = response.data.salary;
        })
        .catch(error => {
          console.error('There was an error!', error);
        });
      fetch('http://127.0.0.1:5555/transactions')
        .then((response) => response.json())
        .then((data) => {
          this.transactions = data.data;
        });
    },
    methods: {
      addTransaction() {
        // Add a new transaction with placeholder data
        const newId = this.transactionIdCounter++;
        this.transactions.push({
          id: newId,
          date: 'YYYY-MM-DD',
          cost: 0,
          item: 'Item name',
          vendor: 'Vendor name',
          category: 'Category name',
        });

        // Set the new transaction to "edit mode"
        this.editMode = { ...this.editMode, [newId]: true };
      },
      editTransaction(id) {
        this.editMode = { ...this.editMode, [id]: true };
      },
      deleteTransaction(id) {
        fetch(`http://127.0.0.1:5555/transactions/${id}`, {
          method: 'DELETE',
        })
        .then(() => {
          this.transactions = this.transactions.filter((transaction) => transaction.id !== id);
        });
      },
      saveTransaction(id) {
        // Exit "edit mode" and save changes to the transaction
        this.editMode = { ...this.editMode, [id]: false };

        // TODO: Save the updated transaction to your backend.
      },
      updateSalary() {
        axios.put('http://127.0.0.1:5555/salary', { salary: this.salary, user_id: 1 })
          .then(() => {
            this.showPopup = true;
            this.editingSalary = false;
            setTimeout(() => {
              this.showPopup = false;
            }, 3000);
          })
          .catch((error) => {
            console.error(error);
          });
      },
    },
  };
</script>

