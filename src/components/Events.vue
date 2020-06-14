<template>
  <v-container>
    <h2>Events</h2>
  </v-container>
</template>

<script>
import { mapState } from "vuex";
export default {
  name: "Events",
  computed: {
    ...mapState(["events"])
  }
};
</script>