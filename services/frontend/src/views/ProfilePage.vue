<template>
  <div
    class="mx-auto text-white flex xl:w-1/3 md:w-1/2 w-2/3 min-h-screen w-full items-center justify-center"
  >
    <div class="shadow-2xl w-full p-20 rounded-md">
      <div class="flex w-full space-y-8 flex-col">
        <div class="text-center text-4xl font-light text-gray-800">
          Your Profile
        </div>

        <div class="flex flex-wrap justify-center">
          <div class="w-8/12 sm:w-6/12 px-2">
            <img
              class="rounded-full align-middle h-auto max-w-full border-none"
              src="https://creative-tim.com/learning-lab/tailwind-starter-kit/img/team-2-800x800.jpg"
            />
          </div>
        </div>

        <div
          class="transform duration-200 text-lg focus-within:border-gray-800 text-gray-800 border-gray-100 w-full border-b-2"
        >
          <input
            v-model="name"
            type="text"
            placeholder="Your Full Name"
            class="text-center w-full border-none bg-transparent outline-none focus:outline-none"
          />
        </div>

        <div
          class="transform duration-200 text-lg focus-within:border-gray-800 text-gray-800 border-gray-100 w-full border-b-2"
        >
          <input
            readonly
            v-model="email"
            type="text"
            placeholder="Your Registered Email ID"
            class="text-center w-full border-none bg-transparent outline-none focus:outline-none"
          />
        </div>

        <div
          class="transform duration-200 text-lg focus-within:border-gray-800 text-gray-800 border-gray-100 w-full border-b-2"
        >
          <input
            v-model="password"
            type="password"
            placeholder="Your Password"
            class="text-center w-full border-none bg-transparent outline-none focus:outline-none"
          />
        </div>

        <div class="grid justify-items-end space-y-2">
          <button
            @click="update_info"
            class="transform w-full duration-200 rounded-sm py-2 px-10 bg-gray-500 hover:bg-gray-800"
          >
            Update Information
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ProfileView",
  components: {},
  data() {
    return {
      name: "",
      email: "",
      password: "",
    };
  },
  methods: {
    update_info() {
      let data = {
        name: this.name,
        email: this.email,
        password: this.password,
      };

      axios({
        method: "post",
        url: "http://127.0.0.1:8001/register",
        data: data,
      })
        .then((response) => {
          this.$store.dispatch("update", data);
          console.log(response);
        })
        .catch(function (response) {
          console.log(response);
        });
    },
  },
  created() {
    this.name = this.$store.state.user.data.name;
    this.email = this.$store.state.user.data.email;
  },
};
</script>

<style lang="scss" scoped></style>
