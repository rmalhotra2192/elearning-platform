<template>
  <div>
    <div
      class="lg:w-4/5 mx-auto grid grid-rows-2 mb-10 lg:grid-rows-none lg:grid-cols-2"
    >
      <div class="grid grid-rows-2 space-y-0">
        <div v-if="current_chapter" class="text-lg self-end">
          <router-link
            :to="{ name: 'detail', params: { courseid: $route.params.c_id } }"
            >
            <div class="flex items-center space-x-2">
              <div class="flex"><svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5"
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  fill-rule="evenodd"
                  d="M10 18a8 8 0 100-16 8 8 0 000 16zm.707-10.293a1 1 0 00-1.414-1.414l-3 3a1 1 0 000 1.414l3 3a1 1 0 001.414-1.414L9.414 11H13a1 1 0 100-2H9.414l1.293-1.293z"
                  clip-rule="evenodd"
                />
              </svg></div>
              <div class="flex">{{ course.title }}</div>
            </div>
          </router-link>
        </div>
        <div v-if="current_chapter" class="text-4xl">
          {{ current_chapter["title"] }}
        </div>
      </div>
      <div class="flex lg:flex-row-reverse gap-2 place-items-center">
        <div>
          <button
            @click="to_next_chapter"
            class="transform flex duration-200 rounded-sm py-2 px-10 bg-blue-400 hover:bg-teal-500 space-x-2 place-items-center text-white"
          >
            <span>Next Chapter </span>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-5 w-5"
              viewBox="0 0 20 20"
              fill="currentColor"
            >
              <path
                fill-rule="evenodd"
                d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-8.707l-3-3a1 1 0 00-1.414 1.414L10.586 9H7a1 1 0 100 2h3.586l-1.293 1.293a1 1 0 101.414 1.414l3-3a1 1 0 000-1.414z"
                clip-rule="evenodd"
              />
            </svg>
          </button>
        </div>
        <div>
          <button
            @click="to_prev_chapter"
            class="transform flex duration-200 rounded-sm py-2 px-10 bg-blue-400 hover:bg-teal-500 space-x-2 place-items-center text-white"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-5 w-5"
              viewBox="0 0 20 20"
              fill="currentColor"
            >
              <path
                fill-rule="evenodd"
                d="M10 18a8 8 0 100-16 8 8 0 000 16zm.707-10.293a1 1 0 00-1.414-1.414l-3 3a1 1 0 000 1.414l3 3a1 1 0 001.414-1.414L9.414 11H13a1 1 0 100-2H9.414l1.293-1.293z"
                clip-rule="evenodd"
              />
            </svg>
            <span> Previous Chapter</span>
          </button>
        </div>
      </div>
    </div>
    <div class="lg:w-4/5 grid mx-auto">
      <content-viewer
        v-if="current_chapter"
        :key="current_chapter.order"
        :chapter="current_chapter"
      ></content-viewer>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ContentViewer from "@/components/Viewer.vue";

export default {
  name: "ViewerView",
  components: { ContentViewer },
  data() {
    return {
      course: null,
      chapters: null,
      current_chapter: null,
    };
  },
  methods: {
    reorder(x, y) {
      if (x.order < y.order) return -1;
      if (x.order > y.order) return 1;
      return 0;
    },
    to_next_chapter() {
      if (this.chapters.length > this.current_chapter.order)
        this.current_chapter = this.chapters[this.current_chapter.order];
    },
    to_prev_chapter() {
      if (this.current_chapter.order > 1)
        this.current_chapter = this.chapters[this.current_chapter.order - 2];
    },
  },
  created() {
    axios
      .get("http://" + location.hostname + ":8000/chapter")
      .then((response) => {
        this.chapters = [];

        for (let chapter of response.data) {
          if (chapter.course_id == this.$route.params.c_id)
            this.chapters.push(chapter);
        }

        this.chapters.sort(this.reorder);

        this.current_chapter = this.chapters[0];
      });

    axios
      .get(
        "http://" +
          location.hostname +
          ":8000/course/" +
          this.$route.params.c_id
      )
      .then((response) => (this.course = response.data));
  },
};
</script>

<style lang="scss" scoped></style>
