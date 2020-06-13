<template>
  <v-app>
    <Header />
    <v-content>
      <router-view :catchUser="catchUser" />
    </v-content>
  </v-app>
</template>

<script>
import { mapActions } from "vuex";
import Header from "./components/Header";
export default {
  name: "App",
  components: {
    Header
  },
  beforeMount() {
    this.checkUser();
  },
  methods: {
    ...mapActions(["checkUser"])
  }
};
</script>
