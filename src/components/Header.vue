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
      to="/"
    >
      <v-icon>mdi-home</v-icon> Home
    </v-btn>
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
    <v-btn
      text
      to="/add-event"
      v-if="user && role === 'Admin'"
    >
      <v-icon>mdi-plus</v-icon> Add Event
    </v-btn>
    <v-btn
      text
      @click.prevent="doLogout"
      v-if="user"
    >
      <v-icon>mdi-logout</v-icon> Logout
    </v-btn>
  </v-app-bar>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  computed: {
    ...mapState(["user", "role", "showMenu"])
  },
  methods: {
    ...mapActions(["doLogout", "openMenu", "closeMenu"])
  }
};
</script>