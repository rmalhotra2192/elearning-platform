<template>
  <footer
    class="lg:w-4/5 mx-auto p-4 bg-white md:flex md:items-center md:justify-between md:p-6 dark:bg-gray-800"
  >
    <span class="text-sm text-gray-500 sm:text-center dark:text-gray-400"
      >© 2022
      <a href="http://mycicdproject.tk" class="hover:underline">Etudier</a>. All
      Rights Reserved.
    </span>
    <ul
      class="flex flex-wrap items-center mt-3 text-sm text-gray-500 dark:text-gray-400 sm:mt-0"
    >
      <li>
        <router-link to="/about" class="mr-4 hover:underline md:mr-6"
          >About</router-link
        >
      </li>
      <li>
        <router-link to="/" class="mr-4 hover:underline md:mr-6"
          >Courses</router-link
        >
      </li>
      <li>
        <router-link to="/login" class="mr-4 hover:underline md:mr-6"
          >Login</router-link
        >
      </li>
    </ul>
  </footer>
</template>

<script>
export default {
  name: "FooterArea",
};
</script>

<style lang="scss" scoped></style>
