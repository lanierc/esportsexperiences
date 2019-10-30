<template>
  <v-app>
    <Header />
    <v-content>
      <HelloWorld />
    </v-content>
  </v-app>
</template>

<script>
import HelloWorld from "./components/HelloWorld";
import Header from "./components/Header";

export default {
  name: "App",
  components: {
    HelloWorld,
    Header
  },
  data: () => ({
    //
  })
};
</script>
