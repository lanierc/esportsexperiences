<template>
  <v-container>
    <h2 class="display-1">Signup</h2>
    <v-form>
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
        :type="show ? 'text' : 'password'"
        prepend-icon="mdi-key"
        :append-icon="show ? 'mdi-eye-off' : 'mdi-eye'"
        @click:append="show = !show"
        v-model="verifyPassword"
      />
      <v-text-field
        label="Username"
        v-model="username"
        prepend-icon="mdi-account"
      />
      <v-text-field
        label="Location"
        v-model="location"
        prepend-icon="mdi-earth"
      />
    </v-form>
  </v-container>
</template>

<script>
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
      success: false,
      loading: false,
      error: null
    };
  }
};
</script>