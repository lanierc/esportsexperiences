<template>
  <v-container>
    <h2 class="display-1">Login</h2>
    <v-form @submit.prevent="loginSubmit">
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
        :loading="loggingIn"
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
import { mapActions, mapState } from "vuex";
export default {
  name: "login",
  props: {
    catchUser: Function
  },
  computed: {
    ...mapState(["errorMessage", "loggingIn"])
  },
  data() {
    return {
      email: "",
      password: "",
      show: false
    };
  },
  methods: {
    ...mapActions(["doLogin"]),
    loginSubmit: function() {
      const { email, password } = this.$data;
      const loginData = { email, password };
      this.doLogin(loginData);
    }
  }
};
</script>