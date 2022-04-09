<template>
  <div class="w-11/12 mx-auto">
    <nav
      class="grid grid-cols-2 bg-white border-gray-200 px-2 py-2.5 rounded dark:bg-gray-800"
    >
      <div
        class="container flex flex-wrap justify-between items-center mx-auto"
      >
        <a href="#" class="flex items-center">
          <img src="../assets/logo.png" class="mr-3 h-6 sm:h-10" />
        </a>
      </div>
      <div class="flex flex-row-reverse gap-2 place-items-center space-x-10">
        <div class="lg:hidden flex justify-end">
          <button class="btn btn-square btn-ghost" @click="toggleNavMenu">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              class="inline-block w-5 h-5 stroke-current"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M4 6h16M4 12h16M4 18h16"
              ></path>
            </svg>
          </button>
        </div>

        <div
          v-if="$store.state.loggedIn"
          class="relative inline-block text-left z-40 mx-10"
        >
          <div>
            <button
              type="button"
              class="inline-flex justify-center w-full rounded-md border border-blue-400 shadow-sm px-4 py-2 bg-white text-sm font-medium text-blue-400 hover:text-blue-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-100 focus:ring-indigo-500"
              @click="toggleUserMenu"
              id="menu-button"
              aria-expanded="true"
              aria-haspopup="true"
            >
              Hi,
              {{
                $store.state.user.data.name.length > 0
                  ? $store.state.user.data.name + "!"
                  : "mate!"
              }}
              <svg
                class="-mr-1 ml-2 h-5 w-5"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
              >
                <path
                  fill-rule="evenodd"
                  d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
                  clip-rule="evenodd"
                />
              </svg>
            </button>
          </div>

          <div
            class="user-personal hidden origin-top-right absolute right-0 mt-2 w-56 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 divide-y divide-gray-100 focus:outline-none"
            role="menu"
            aria-orientation="vertical"
            aria-labelledby="menu-button"
            tabindex="-1"
          >
            <div class="py-1" role="none">
              <router-link
                to="/profile/"
                href="#"
                class="text-gray-700 block px-4 py-2 text-sm"
                role="menuitem"
                tabindex="-1"
                id="menu-item-0"
                >Profile</router-link
              >
              <a
                @click="logout"
                href="#"
                class="text-gray-700 block px-4 py-2 text-sm"
                role="menuitem"
                tabindex="-1"
                id="menu-item-1"
                >Signout</a
              >
            </div>
          </div>
        </div>

        <div v-if="!$store.state.loggedIn" class="hidden lg:flex mx-10">
          <router-link to="/login">
            <button
              class="transform flex duration-200 rounded-md py-1 px-4 text-blue-400 border-2 border-blue-400 hover:bg-blue-400 space-x-2 place-items-center hover:text-white"
            >
              <span>Login</span>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-6 w-6"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                stroke-width="2"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1"
                />
              </svg>
            </button>
          </router-link>
        </div>

        <div v-if="!$store.state.loggedIn" class="hidden lg:flex">
          <router-link
            class="transform duration-200 hover:border-bottom-2 hover:text-blue-400 cursor-pointer"
            to="/signup/"
            >Register</router-link
          >
        </div>

        <div class="hidden lg:flex">
          <router-link
            class="transform duration-200 hover:border-bottom-2 hover:text-blue-400 cursor-pointer"
            to="/"
            >Courses</router-link
          >
        </div>

        <div class="hidden lg:flex">
          <router-link
            class="transform duration-200 hover:border-bottom-2 hover:text-blue-400 cursor-pointer"
            to="/about"
            >About</router-link
          >
        </div>
      </div>

      <div
        class="mobile-menu w-60 h-screen z-50 shadow-md bg-white px-1 absolute inset-y-0 right-0 h-screen hidden"
      >
        <ul class="relative">
          <li class="relative flex justify-end">
            <button class="btn btn-square btn-ghost m-5" @click="toggleNavMenu">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5"
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  fill-rule="evenodd"
                  d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                  clip-rule="evenodd"
                />
              </svg>
            </button>
          </li>
          <li class="relative">
            <router-link
              class="flex items-center py-4 px-6 h-12 text-ellipsis text-sm hover:text-gray-900 hover:bg-gray-100 transition duration-300 ease-in-out hover:border-bottom-2 hover:text-blue-400 cursor-pointer"
              to="/about"
              >About</router-link
            >
          </li>
          <li class="relative">
            <router-link
              class="flex items-center py-4 px-6 h-12 text-ellipsis text-sm hover:text-gray-900 hover:bg-gray-100 transition duration-300 ease-in-out hover:border-bottom-2 hover:text-blue-400 cursor-pointer"
              to="/"
              >Courses</router-link
            >
          </li>
          <li class="relative">
            <router-link
              class="flex py-4 px-6 h-12 text-ellipsis text-sm hover:text-gray-900 hover:bg-gray-100 transition duration-300 ease-in-out hover:border-bottom-2 hover:text-blue-400 cursor-pointer"
              to="/signup/"
              >Register</router-link
            >
          </li>
          <li class="relative">
            <router-link
              class="flex py-4 px-6 h-12 text-ellipsis text-sm hover:text-gray-900 hover:bg-gray-100 transition duration-300 ease-in-out hover:border-bottom-2 hover:text-blue-400 cursor-pointer"
              to="/login"
              >Login</router-link
            >
          </li>
        </ul>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: "NavigationBar",
  methods: {
    toggleUserMenu: function () {
      let elem = document.getElementsByClassName("user-personal")[0];
      elem.classList.toggle("hidden");
    },
    toggleNavMenu: function () {
      let elem_mobile = document.getElementsByClassName("mobile-menu")[0];
      elem_mobile.classList.toggle("hidden");
    },
    logout: function () {
      this.$store.dispatch("logout");
      this.$router.push({ name: "courses" });
    },
  },
};
</script>

<style lang="scss" scoped></style>
