<template>
  <v-app-bar
    color="primary"
    dark
    app
  >
    <v-app-bar-nav-icon />
    <v-toolbar-title>Esports Experiences</v-toolbar-title>
    <v-spacer />
    <v-btn
      text
      to="/login"
      v-if="!user"
    >
      <v-icon>mdi-login</v-icon> Login
    </v-btn>
    <v-btn
      text
      to="/signup"
      v-if="!user"
    >
      <v-icon>mdi-account-plus</v-icon> Signup
    </v-btn>
  </v-app-bar>
</template>

<script>
export default {
  name: "header",
  props: {
    user: String,
    role: String
  }
};
</script>