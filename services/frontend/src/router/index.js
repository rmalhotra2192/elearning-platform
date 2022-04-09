import { createRouter, createWebHistory } from "vue-router";
import DetailsPage from "../views/DetailsPage.vue";
import LoginPage from "../views/LoginPage.vue";
import SignupPage from "../views/SignupPage.vue";
import ProfilePage from "../views/ProfilePage.vue";
import ListPage from "../views/ListPage.vue";
import ViewerPage from "../views/ViewerPage.vue";
import ForgotPasswordPage from "../views/ForgotPasswordPage.vue";
import store from "@/store";

const routes = [
  {
    path: "/",
    name: "courses",
    component: ListPage,
  },
  {
    path: "/detail/:courseid",
    name: "detail",
    component: DetailsPage,
    beforeEnter: (to, from) => {
      console.log(to, from);
      if (store.state.loggedIn) return true;
      else {
        router.push({ name: "login" });
        return false;
      }
    },
  },
  {
    path: "/viewer/:c_id",
    name: "viewer",
    component: ViewerPage,
    beforeEnter: (to, from) => {
      console.log(to, from);
      if (store.state.loggedIn) return true;
      else {
        router.push({ name: "login" });
        return false;
      }
    },
  },
  {
    path: "/login",
    name: "login",
    component: LoginPage,
    beforeEnter: (to, from) => {
      console.log(to, from);
      if (store.state.loggedIn) return false;
      return true;
    },
  },
  {
    path: "/signup",
    name: "signup",
    component: SignupPage,
    beforeEnter: (to, from) => {
      console.log(to, from);
      if (store.state.loggedIn) return false;
      return true;
    },
  },
  {
    path: "/profile/",
    name: "profile",
    component: ProfilePage,
    beforeEnter: (to, from) => {
      console.log(to, from);
      if (store.state.loggedIn) return true;
      else {
        router.push({ name: "login" });
        return false;
      }
    },
  },
  {
    path: "/resetpassword",
    name: "resetpassword",
    component: ForgotPasswordPage,
    beforeEnter: (to, from) => {
      console.log(to, from);
      if (store.state.loggedIn) return false;
      return true;
    },
  },
  // {
  //   path: "/about",
  //   name: "about",
  //   component: ListPage,
  // },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
