<template>
  <v-container>
    <div class="home">
      <h1>Esports Experiences</h1>
      <Events />
    </div>
  </v-container>
</template>

<script>
import { mapActions } from "vuex";
import Events from "./Events";

export default {
  name: "home",
  beforeMount() {
    this.getEvents();
  },
  components: {
    Events
  },
  methods: {
    ...mapActions(["getEvents"])
  }
};
</script>
