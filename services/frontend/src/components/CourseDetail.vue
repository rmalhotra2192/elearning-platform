<template>
  <div>
    <div class="my-10">
      <h1 class="text-3xl">{{ course.title }}</h1>
    </div>
    <div class="text-lg mt-10 font-bold">Course Description</div>
    <div class="text-lg space-y-10 leading-relaxed">
      {{ course.description }}
    </div>
    <div class="text-lg mt-10 font-bold">Chapters in the course</div>
    <ul class="list-outside">
      <li v-for="chapter in chapters" :key="chapter.id" class="my-2 text-md">
        {{ "Chapter " + chapter.order + ". " + chapter.title }}
      </li>
    </ul>
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
    chapters: {
      type: Object,
      default: null,
    },
  },
};
</script>

<style lang="scss" scoped></style>
