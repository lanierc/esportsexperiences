<template>
  <v-container>
    <h2 class="display-1">Login</h2>
    <v-form @submit.prevent="doLogin">
      <v-text-field
        label="Email Address"
        v-model="email"
        prepend-icon="mdi-email"
      />
      <v-text-field
        :type="show ? 'text' : 'password'"
        :append-icon="show ? 'mdi-eye-off' : 'mdi-eye'"
        v-model="password"
        label="Password"
        prepend-icon="mdi-key"
        @click:append="show = !show"
      />
      <v-btn
        color="primary"
        dark
        :loading="loading"
        type="submit"
      >
        <v-icon>mdi-login</v-icon> Sign In
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
export default {
  name: "login",
  data() {
    return {
      email: "",
      password: "",
      loading: false,
      show: false
    };
  },
  methods: {
    doLogin: async function() {
      this.loading = true;
    }
  }
};
</script>