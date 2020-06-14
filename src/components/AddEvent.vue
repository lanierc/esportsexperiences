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
import { mapState, mapActions } from "vuex";
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
  },
  methods: {
    ...mapActions(["addEvent"]),
    submitEvent: function() {
      const { name, location, description, genre } = this.$data;
      const { user, role } = this;
      let { website, facebook, twitter, instagram } = this.$data;
      const websiteIndex =
        website.indexOf("http://") || website.indexOf("https://");
      if (websiteIndex === -1) {
        website = `http://${website}`;
      }
      const facebookIndex =
        facebook.indexOf("https://") || facebook.indexOf("http://");
      if (facebookIndex === -1) {
        facebook = `https://${facebook}`;
      }
      const twitterIndexInsecure = twitter.indexOf("http://twitter.com/");
      const twitterIndexSecure = twitter.indexOf("https://twitter.com/");
      if (twitterIndexInsecure !== -1) {
        twitter.replace("http://twitter.com/", "");
      } else if (twitterIndexSecure !== -1) {
        twitter.replace("https://twitter.com/", "");
      }
      const instagramIndexInsecure = instagram.indexOf("http://instagram.com/");
      const instagramIndexSecure = instagram.indexOf("https://instagram.com/");
      if (instagramIndexInsecure !== -1) {
        instagram.replace("http://instagram.com", "");
      } else if (instagramIndexSecure !== -1) {
        instagram.replace("https://instagram.com", "");
      }
      const submitData = {
        name,
        location,
        description,
        genre,
        user,
        role,
        website,
        facebook,
        instagram,
        twitter
      };
      this.addEvent(submitData);
    }
  }
};
</script>