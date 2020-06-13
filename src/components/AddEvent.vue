<template>
  <v-container>
    <div class="add-event">
      <h1>Add Event</h1>
      <v-form>

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
      loading: false
    };
  },
  computed: {
    ...mapState(["user", "role"])
  }
};
</script>