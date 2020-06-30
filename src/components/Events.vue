<template>
  <v-container>
    <h2>Events</h2>
    <div v-for="(event, index) in events" :key="index">
      <h2>{{event.name}}</h2>
      <p class="subtext">{{event.location}}</p>
    </div>
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

<style>
.subtext {
  font-size: 0.8rem;
}
</style>
