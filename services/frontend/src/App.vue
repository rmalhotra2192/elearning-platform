<template>
  <div class="flex flex-col h-screen">
    <navigation-bar></navigation-bar>
    <router-view class="mb-auto" />
    <footer-area class="mt-20"></footer-area>
  </div>
</template>

<script>
import NavigationBar from "@/components/Header.vue";
import FooterArea from "@/components/Footer.vue";
export default {
  components: {
    NavigationBar,
    FooterArea,
  },
};
</script>

<style></style>
