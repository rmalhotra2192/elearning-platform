<template>
  <div>
    <div class="my-10">
      <h1 class="text-3xl">{{ course.title }}</h1>
    </div>
    <div class="space-y-10" v-html="course.description"></div>
  </div>
</template>

<script>
export default {
  name: "DetailDescription",
  props: {
    course: {
      type: Object,
      default: null,
    },
  },
};
</script>

<style lang="scss" scoped></style>
