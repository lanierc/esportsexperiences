import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
import router from "../router";
import { setToken, removeToken } from "../services/tokenService";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    loggingIn: false,
    errorMessage: null,
    user: null,
    role: null,
    showMenu: false,
    events: [],
  },
  mutations: {
    loginStart: (state) => {
      state.loggingIn = true;
    },
    loginStop: (state, errorMessage) => {
      state.loggingIn = false;
      state.errorMessage = errorMessage;
    },
    updateUser: (state, user) => {
      state.user = user.id;
      state.role = user.role;
    },
    logout: (state) => {
      state.user = null;
      state.role = null;
    },
    updateMenu: (state, bool) => {
      state.showMenu = bool;
    },
    setEvents: (state, arr) => {
      state.events = arr;
    },
  },
  actions: {
    doLogout: ({ commit }) => {
      commit("updateUser", { id: null, role: null });
      removeToken();
      localStorage.removeItem("esxId");
    },
    openMenu: ({ commit }) => {
      commit("updateMenu", true);
    },
    closeMenu: ({ commit }) => {
      commit("updateMenu", false);
    },
    doLogin: async ({ commit }, loginData) => {
      commit("loginStart");
      const { email, password } = loginData;

      const res = await axios({
        method: "POST",
        url: "/api/users/login",
        data: {
          email,
          password,
        },
      });
      const { token } = res.data;
      const id = res.data.data._id.$oid;
      const { role } = res.data.data;
      setToken(token);
      localStorage.setItem("esxId", id);
      commit("updateUser", { id, role });
      commit("loginStop", null);
      router.push("/");
    },
    checkUser: async ({ commit }) => {
      const id = localStorage.getItem("esxId");
      if (id !== null) {
        const res = await axios.get(`/api/users/${id}`);
        const { role } = res.data.data;
        commit("updateUser", { id, role });
      }
    },
    // eslint-disable-next-line no-unused-vars
    addEvent: async ({ commit }, formData) => {
      const {
        user,
        name,
        location,
        description,
        genre,
        facebook,
        twitter,
        instagram,
        website,
      } = formData;
      const res = await axios({
        method: "POST",
        url: "/api/events",
        data: {
          user,
          name,
          location,
          description,
          genre,
          facebook,
          twitter,
          instagram,
          website,
        },
      });
      console.log(res.data.data);
    },
    getEvents: async ({ commit }) => {
      const res = await axios({
        method: "GET",
        url: "/api/events",
      });
      commit("setEvents", res.data.data);
    },
  },
  modules: {},
});
