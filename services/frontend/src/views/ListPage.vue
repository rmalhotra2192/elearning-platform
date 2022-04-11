<template>
  <div class="lg:w-4/5 mx-auto">
    <div class="my-10">
      <h1 class="text-4xl">All Available Courses</h1>
      <hr class="my-2 border-gray-400 border-dashed" />
    </div>
    <div>
      <div v-for="course in courses_for_current_page" :key="course.id">
        <course-list :course="course"></course-list>
      </div>
      <div
        v-if="total_pages > 1"
        class="flex lg:flex-row-reverse gap-2 place-items-center"
      >
        <div>
          <button
            @click="to_next_page"
            class="transform flex duration-200 rounded-lg py-2 px-5 bg-blue-400 hover:bg-teal-500 space-x-2 place-items-center text-white"
          >
            <span>Next Page</span>
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
            @click="to_prev_page"
            class="transform flex duration-200 rounded-lg py-2 px-5 bg-blue-400 hover:bg-teal-500 space-x-2 place-items-center text-white"
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
            <span>Previous Page</span>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import CourseList from "@/components/CourseList.vue";

export default {
  name: "ListView",
  data() {
    return {
      courses: [],
      courses_for_current_page: [],
      current_page: 0,
      courses_per_page: 4,
    };
  },
  components: {
    CourseList,
  },
  methods: {
    to_next_page() {
      if (this.current_page < this.total_pages - 1) {
        ++this.current_page;
        this.get_courses_for_current_page();
      }
    },
    to_prev_page() {
      if (this.current_page > 0) {
        --this.current_page;
        this.get_courses_for_current_page();
      }
    },
    get_courses_for_current_page() {
      this.courses_for_current_page = [];

      if (this.courses.length <= this.courses_per_page) {
        this.courses_for_current_page = this.courses;
        return;
      }

      for (let x = 0; x < this.courses_per_page; x++) {
        if (
          x + this.current_page * this.courses_per_page <
          this.courses.length
        ) {
          this.courses_for_current_page.push(
            this.courses[x + this.current_page * this.courses_per_page]
          );
        } else {
          break;
        }
      }
    },
  },
  computed: {
    total_pages() {
      return Math.ceil(this.courses.length / this.courses_per_page);
    },
  },
  mounted() {
    axios
      .get("http://" + location.hostname + ":8000/course")
      .then((response) => {
        this.courses = response.data;
        this.get_courses_for_current_page();
      });
  },
};
</script>

<style lang="scss" scoped></style>
