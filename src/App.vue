<template>
  <v-app>
    <Header />
    <v-content>
      <router-view />
    </v-content>
  </v-app>
</template>

<script>
import Header from "./components/Header";
import axios from "axios";

export default {
  name: "App",
  components: {
    Header
  },
  data() {
    return {
      user: null,
      role: null
    };
  },
  beforeMount() {
    const user = localStorage.getItem("esxId");
    this.user = user;
  },
  mounted() {
    this.checkPermission();
  },
  methods: {
    catchUser: function(id) {
      this.user = id;
      this.checkPermission();
    },
    checkPermission: async function() {
      const { user } = this.$data;
      if (!user) {
        this.role = null;
      } else {
        const userData = await axios.get(`/api/users/${user}`);
        const { role } = userData.data.data;
        this.role = role;
      }
    }
  }
};
</script>
