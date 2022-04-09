<template>
  <div
    class="mx-auto text-white flex xl:w-1/3 md:w-1/2 w-2/3 min-h-screen w-full items-center justify-center"
  >
    <div class="shadow-2xl w-full p-20 rounded-md">
      <div class="flex w-full space-y-8 flex-col">
        <div class="text-center text-4xl font-light text-gray-800">
          Reset Your Password
        </div>
        <div
          class="transform duration-200 text-lg focus-within:border-gray-800 text-gray-800 border-gray-100 w-full border-b-2"
        >
          <input
            type="text"
            placeholder="Your Registered Email ID"
            class="w-full border-none bg-transparent outline-none focus:outline-none"
          />
        </div>

        <div class="grid justify-items-end space-y-2">
          <button
            class="transform flex duration-200 rounded-sm py-2 px-10 bg-gray-500 hover:bg-gray-800"
          >
            Send me Password Reset Link
          </button>
        </div>

        <div class="text-center text-lg">
          <p>
            <span class="font-light text-gray-500"
              >Go Back to<router-link
                to="/login"
                class="font-light transform duration-200 hover:underline hover:text-gray-800 text-gray-500"
              >
                Login</router-link
              >
              Page</span
            >
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ForgotPasswordView",
  components: {},
};
</script>

<style lang="scss" scoped></style>
