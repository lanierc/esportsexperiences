<template>
  <v-container>
    <h2 class="display-1">Login</h2>
    <v-form @submit.prevent="doLogin">
      <v-text-field
        label="Email Address"
        v-model="email"
        prepend-inner-icon="mdi-email"
      />
      <v-text-field
        type="password"
        v-model="password"
        label="Password"
        prepend-inner-icon="mdi-key"
      />
      <v-btn
        color="primary"
        dark
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
      password: ""
    };
  },
  methods: {
    doLogin: async function() {}
  }
};
</script>