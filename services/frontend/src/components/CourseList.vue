<template>
  <div class="space-y-10 mb-10">
    <div class="grid grid-cols-12 space-x-10">
      <div class="col-span-2">
        <img class="w-full rounded-md" :src="course.image_url" />
      </div>
      <div class="col-span-10">
        <div class="text-2xl">
          <router-link
            :to="{ name: 'detail', params: { courseid: course.id } }"
            >{{ course.title }}</router-link
          >
        </div>
        <div class="text-sm">
          {{ course.description }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CourseList",
  props: {
    course: {
      type: Object,
    },
  },
};
</script>

<style lang="scss" scoped></style>
