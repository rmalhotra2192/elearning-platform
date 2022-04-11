<template>
  <div class="w-10/12 mx-auto grid grid-cols-12 space-x-10">
    <detail-description
      v-if="course"
      :course="course"
      :chapters="chapters"
      class="col-span-12 lg:col-span-10"
    ></detail-description>
    <div class="col-span-12 lg:col-span-2">
      <div class="my-10 flex justify-end lg:justify-none lg:grow">
        <router-link
          :to="{ name: 'viewer', params: { c_id: $route.params.courseid } }"
          ><button
            class="transform flex grow duration-200 rounded-lg py-2 px-5 bg-blue-400 hover:bg-teal-500 space-x-2 place-items-center text-white"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-5 w-5"
              viewBox="0 0 20 20"
              fill="currentColor"
            >
              <path
                fill-rule="evenodd"
                d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-11a1 1 0 10-2 0v2H7a1 1 0 100 2h2v2a1 1 0 102 0v-2h2a1 1 0 100-2h-2V7z"
                clip-rule="evenodd"
              />
            </svg>
            <span>Start Learning</span>
          </button></router-link
        >
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import DetailDescription from "@/components/CourseDetail.vue";

export default {
  name: "DetailsView",
  components: { DetailDescription },
  data() {
    return {
      course: null,
      chapters: null,
    };
  },
  methods: {
    reorder(x, y) {
      if (x.order < y.order) return -1;
      if (x.order > y.order) return 1;
      return 0;
    },
  },
  created() {
    axios
      .get(
        "http://" +
          location.hostname +
          ":8000/course/" +
          this.$route.params.courseid
      )
      .then((response) => (this.course = response.data));

    axios
      .get("http://" + location.hostname + ":8000/chapter/")
      .then((response) => {
        this.chapters = [];

        for (let chapter of response.data) {
          if (chapter.course_id == this.$route.params.courseid)
            this.chapters.push(chapter);
        }

        this.chapters.sort(this.reorder);
      });
  },
};
</script>

<style lang="scss" scoped></style>
