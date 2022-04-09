<template>
  <div class="mx-10 my-5">
    <div class="space-y-4 mx-auto lg:w-8/12" v-html="chapter['content']"></div>
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
