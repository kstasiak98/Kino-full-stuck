import Vue from "vue";
import Router from "vue-router";
import HomePage from "../components/HelloWorld.vue";
import RepertoirePage from "@/components/films/RepertoirePage";
import ShopPage from "@/components/seanse/ShopPage";
import TicketPage from "@/components/shop/TicketPage";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "Home",
      component: HomePage
    },
    {
      path: "/repertoire",
      name: "Repertoire",
      component: RepertoirePage
    },
    {
      path: "/store",
      name: "Store",
      component: ShopPage
    },
    {
      path: "/ticket",
      name: "Ticket",
      component: TicketPage
    }
  ]
});
