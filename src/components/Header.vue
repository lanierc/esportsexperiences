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