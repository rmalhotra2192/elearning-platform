<template>
  <div class="space-y-10 mb-10">
    <div class="grid grid-cols-12 space-x-10">
      <div class="col-span-2">
        <router-link
            :to="{ name: 'detail', params: { courseid: course.id } }"
            ><img class="w-full rounded-md" :src="course.image_url" /></router-link
          >
      </div>
      <div class="col-span-10 space-y-4">
        <div class="text-3xl">
          <router-link
            :to="{ name: 'detail', params: { courseid: course.id } }"
            >{{ course.title }}</router-link
          >
        </div>
        <div class="text-sm leading-relaxed">
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
