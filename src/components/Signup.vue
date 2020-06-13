<template>
  <v-container>
    <h2 class="display-1">Signup</h2>
    <v-form @submit.prevent="createAccount">
      <v-text-field
        label="Email Address"
        v-model="email"
        prepend-icon="mdi-email"
      />
      <v-text-field
        label="Password"
        :type="show ? 'text' : 'password'"
        prepend-icon="mdi-key"
        :append-icon="show ? 'mdi-eye-off' : 'mdi-eye'"
        @click:append="show = !show"
        v-model="password"
      />
      <v-text-field
        label="Verify Password"
        :type="showVerify ? 'text' : 'password'"
        prepend-icon="mdi-key"
        :append-icon="showVerify ? 'mdi-eye-off' : 'mdi-eye'"
        @click:append="showVerify = !showVerify"
        v-model="verifyPassword"
      />
      <v-text-field
        label="Username"
        v-model="username"
        prepend-icon="mdi-account"
      />
      <v-text-field
        label="Real Name"
        v-model="realName"
        prepend-icon="mdi-account-details"
      />
      <v-text-field
        label="Location"
        v-model="location"
        prepend-icon="mdi-earth"
      />
      <v-btn
        color="primary"
        dark
        :loading="loading"
        type="submit"
      >
        <v-icon>mdi-account-plus</v-icon> Register
      </v-btn>
      <v-btn
        text
        to="/"
      >
        <v-icon>mdi-arrow-left</v-icon> Back
      </v-btn>
    </v-form>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  name: "signup",
  data() {
    return {
      email: "",
      password: "",
      verifyPassword: "",
      username: "",
      location: "",
      show: false,
      showVerify: false,
      success: false,
      loading: false,
      error: null,
      realName: ""
    };
  },
  methods: {
    createAccount: async function() {
      this.loading = true;
      const {
        username,
        email,
        password,
        verifyPassword,
        location,
        realName: real_name
      } = this.$data;
      if (password !== verifyPassword) {
        this.error = "Your passwords do not match.";
        this.loading = false;
        return;
      }
      try {
        const res = await axios({
          method: "POST",
          url: "/api/users/signup",
          data: {
            username,
            email,
            password,
            location,
            real_name
          }
        });
        if (res) {
          this.loading = false;
          this.success = true;
        }
      } catch (e) {
        this.error = e;
        this.loading = false;
      }
    }
  }
};
</script>
