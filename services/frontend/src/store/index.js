import { createStore } from "vuex";
import createPersistedState from "vuex-persistedstate";

export default createStore({
  state: {
    user: {},
    access_token: "",
    token_type: "",
    loggedIn: false,
  },
  getters: {},
  mutations: {
    LOG_IN(state, payload) {
      state.loggedIn = true;
      state.user = payload.user;
      state.token_type = payload.token_type;
      state.access_token = payload.access_token;
    },
    LOG_OUT(state) {
      state.loggedIn = false;
      state.user = {};
      state.token_type = "";
      state.access_token = "";
    },
    UPDATE(state, payload) {
      if (payload.name.length > 0) {
        state.user.data.name = payload.name;
      }
    },
  },
  actions: {
    login({ state, commit }, payload) {
      if (!state.loggedIn) {
        commit("LOG_IN", payload);
      }
    },
    logout({ state, commit }) {
      if (state.loggedIn) {
        commit("LOG_OUT");
      }
    },
    update({ state, commit }, payload) {
      if (state.loggedIn) {
        commit("UPDATE", payload);
      }
    },
  },
  modules: {},
  plugins: [createPersistedState()],
});
