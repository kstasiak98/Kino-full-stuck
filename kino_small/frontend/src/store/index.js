import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    cart: []
  },
  mutations: {
    addTicketArrayToCart(state, ticketArray) {
      ticketArray.forEach(ticket => state.cart.push(ticket));
    },
    addTicketToCart(state, ticket) {
      state.cart.push(ticket);
    },
    removeTicketFromCart(state) {
      state.cart.pop();
    }
  },
  actions: {},
  modules: {}
});
