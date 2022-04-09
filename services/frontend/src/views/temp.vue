<template>
  <div
    class="mx-auto text-white flex xl:w-1/3 md:w-1/2 w-2/3 min-h-screen w-full items-center justify-center"
  >
    <div class="shadow-2xl w-full p-20 rounded-md">
      <div class="flex w-full space-y-8 flex-col">
        <div class="text-center text-4xl font-light text-gray-800">Sign In</div>
        <div
          class="transform duration-200 text-lg focus-within:border-gray-800 text-gray-800 border-gray-100 w-full border-b-2"
        >
          <input
            type="text"
            placeholder="Your Registered Email ID"
            v-model="email"
            class="w-full border-none bg-transparent outline-none focus:outline-none"
          />
        </div>

        <div
          class="transform duration-200 text-lg focus-within:border-gray-800 text-gray-800 border-gray-100 w-full border-b-2"
        >
          <input
            type="password"
            placeholder="Your Password"
            v-model="password"
            class="w-full border-none bg-transparent outline-none focus:outline-none"
          />
        </div>

        <div class="grid justify-items-end space-y-2">
          <button
            @click="login"
            class="transform flex duration-200 rounded-sm py-2 px-10 bg-gray-500 hover:bg-gray-800"
          >
            Sign In
          </button>
          <router-link
            to="/resetpassword"
            class="transform text-center text-gray-500 duration-200 hover:text-gray-800 font-light"
            >Forgot password?</router-link
          >
        </div>

        <div class="text-center text-lg">
          <p>
            <span class="font-light text-gray-500"
              >Don't have an account?<router-link
                to="/signup"
                class="font-light transform duration-200 hover:underline hover:text-gray-800 text-gray-500"
              >
                Sign up.</router-link
              ></span
            >
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "LoginView",
  data() {
    return {
      email: "",
      password: "",
      access_token: "",
    };
  },
  components: {},
  methods: {
    login() {
      let body = new FormData();
      body.append("username", this.email);
      body.append("password", this.password);

      axios({
        method: "post",
        url: "http://127.0.0.1:8001/token",
        data: body,
        headers: { "Content-Type": "multipart/form-data" },
      })
        .then((response) => {
          this.access_token = response["data"]["access_token"];
        })
        .catch(function (response) {
          console.log(response);
        });
    },
  },
};
</script>

<style lang="scss" scoped></style>
