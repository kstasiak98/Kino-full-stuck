<template>
  <v-container>
    Wybrany seans: {{SeansIDnew}}
    Wybrany film: {{film}}
    wybrana sala: {{sall}}
    {{SeansIDnew.seans_film}}

    Miejsca zarezerwowane: {{Reserved_tabel}}

<!--    {{ Seans }}-->
    <v-row align-content="center" justify="center">
      <v-card align="center" class="pa-2">
        <div class="rectangle">EKRAN</div>
        <v-layout v-for="Row in sall.number_of_rows" :key="Row">
          <FpToggle
            :lay="get_letter_by_id(Row - 1)"
            :places="sall.number_of_columns"
            @bind_methods="SetTable"
            :reserved="Reserved_tabel"
          ></FpToggle>
        </v-layout>
<!--        <v-btn @click="showTable">CHECK</v-btn>-->
        <v-btn @click="AddTicket">KUP BILETY</v-btn>
      </v-card>
    </v-row>
  </v-container>
</template>

<script>
import FpToggle from "@/FPcomponents/FpToggle.vue";
import {apiService} from "@/common/api.service";

export default {
  name: "SallPage",
  components: { FpToggle },
  props: ["Sala", "Seans", "SeansIDnew", "Reserved_tabel"],
  data: () => ({
    tabel_choesen_seats: [],
      sall: [],
      film: [],
      tickets1: [],
  }),
  mounted() {
    this.getFilm();
    this.getSall();
      this.MakeArray();

      // this.MakeNewArray();
  },
    watch: {
      SeansIDnew: {
          deep: true,
          handler() {
              this.getFilm();
              this.getSall();
          }
      }
    },


  methods: {
      getFilm() {
          let endpoint = `api/films/${this.SeansIDnew.seans_film}/`;
          apiService(endpoint)
              .then(data => {
                  this.film = data;
              })
      },
      getSall() {
          let endpoint = `api/sall/${this.SeansIDnew.seans_sall}/`;
          console.log(endpoint)
          apiService(endpoint)
              .then(data => {
                  this.sall = data;
              })
      },



    MakeArray() {
      this.tabel_choesen_seats = new Array(this.Sala.rows);
    },
      makeReservePlaces() {

      },
      // MakeNewArray() {
      //     this.tabel_choesen_seats = new Array(this.sall.number_of_rows);
      // },
    get_letter_by_id(id) {
      return String.fromCharCode(65 + id);
    },
    showTable() {
      console.log(this.tabel_choesen_seats);
    },
    SetTable(e, y) {
      let newArray = new Array();
      newArray = this.tabel_choesen_seats;
      let row = y.charCodeAt();
      row = row - 65;
      newArray[row] = { miejsca: e };
      this.tabel_choesen_seats = newArray;
    },
    AddTicket() {
      const newTicket = {
        seans: this.SeansIDnew,
          film_name: this.film.title,
        miejsca: this.tabel_choesen_seats
      };
      this.$store.commit("addTicketToCart", newTicket);
      this.$router.push({
        path: "/ticket"
      });
    }
  }
};
</script>

<style scoped>
.rectangle {
  width: 60%;
  background-color: lightgrey;
  text-align: center;
  margin: auto;
}
</style>
