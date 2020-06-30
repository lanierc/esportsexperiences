<template>
  <v-container>
    <h2>Events</h2>
    <div v-for="(event, index) in events" :key="index">
      <h2>{{event.name}}</h2>
      <p class="subtext">{{event.location}}</p>
      <p v-if="event.owner && event.owner !== ''"><span class="subheading">Owner:</span> {{event.owner}}</p>
      <h3>About this event:</h3>
      <p>{{event.description}}</p>
      <p>
        <span class="subtext">Social Links:</span> 
	<v-btn text :href="event.website"><v-icon>mdi-web</v-icon></v-btn>
	<v-btn text :href="event.facebook"><v-icon>mdi-facebook</v-icon></v-btn>
	<v-btn text :href="`https://twitter.com/${event.twitter}`"><v-icon>mdi-twitter</v-icon></v-btn>
	<v-btn text :href="`https://twitter.com/${event.instagram}`"><v-icon>mdi-instagram</v-icon></v-btn>
      </p>
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
