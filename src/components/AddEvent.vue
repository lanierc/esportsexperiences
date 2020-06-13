<template>
  <v-container>
    <div class="add-event">
      <h1>Add Event</h1>
      <v-form @submit.prevent="submitEvent">
        <v-text-field
          v-model="name"
          label="Event Name"
          prepend-icon="mdi-calendar-blank-outline"
        />
        <v-text-field
          v-model="location"
          label="Event Location"
          prepend-icon="mdi-earth"
        />
        <v-textarea
          label="Description"
          v-model="description"
          prepend-icon="mdi-comment-text-outline"
        />
        <v-text-field
          label="Website"
          v-model="website"
          prepend-icon="mdi-web"
        />
        <v-text-field
          label="Facebook (Full URL)"
          v-model="facebook"
          prepend-icon="mdi-facebook"
        />
        <v-text-field
          label="Twitter (Username Only)"
          v-model="twitter"
          prepend-icon="mdi-twitter"
        />
        <v-text-field
          label="Instagram (Username Only)"
          v-model="instagram"
          prepend-icon="mdi-instagram"
        />
        <v-select
          :items="genres"
          v-model="genre"
          label="Genre"
          prepend-icon="mdi-palette-swatch"
        />
        <v-btn
          type="submit"
          color="primary"
        >Submit Event</v-btn>
      </v-form>
    </div>
  </v-container>
</template>

<script>
import { mapState } from "vuex";
export default {
  name: "add-event",
  data() {
    return {
      name: "",
      location: "",
      description: "",
      website: "",
      facebook: "",
      twitter: "",
      instagram: "",
      genre: "",
      loading: false,
      genres: [
        "Fighting Games",
        "DOTA",
        "League of Legends",
        "Hearthstone",
        "FPS",
        "Various"
      ]
    };
  },
  computed: {
    ...mapState(["user", "role"])
  }
};
</script>