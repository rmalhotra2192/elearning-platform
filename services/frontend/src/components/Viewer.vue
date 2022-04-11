<template>
  <div class="my-5 mx-auto">
    <div class="space-y-4 mx-auto" v-html="chapter['content']"></div>
  </div>
</template>

<script>
export default {
  name: "ContentViewer",
  props: {
    chapter: {
      type: Object,
      default: null,
    },
  },
};
</script>

<style lang="scss" scoped></style>
