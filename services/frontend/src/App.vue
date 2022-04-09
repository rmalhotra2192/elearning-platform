<template>
  <div>
    <navigation-bar></navigation-bar>
    <router-view />
  </div>
</template>

<script>
import NavigationBar from "@/components/Header.vue";
export default {
  components: {
    NavigationBar,
  },
};
</script>

<style></style>
