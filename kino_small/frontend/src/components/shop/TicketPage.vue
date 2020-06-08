<template>
  <v-container>
    <v-row class="text-center" justify="center">
      <v-col>
        <p>BILETY:</p>
      </v-col>
      {{cart[0]}}
      <v-row>
        {{cart[0].seans.seans_film}}
      </v-row>
      <v-row>
        {{cart[0].miejsca}}
      </v-row>
<!--      <v-row v-for="(ticket, index) in cart"  :key="index">-->
<!--        <v-card>-->
<!--          <h3> TYTUL: {{ticket.seans.film.title}}</h3>-->
<!--          <p>Data: <b>{{ticket.seans.date}}</b></p>-->
<!--          <p>Godzina: <b>{{ticket.seans.time}}</b></p>-->
<!--          <p>Miejsca: {{ticket.miejsca}}</p>-->
<!--        </v-card>-->
<!--      </v-row>-->
    </v-row>
    <v-row class="text-center" justify="center">
      <v-btn>ZAPALAC</v-btn>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "TicketPage",

  data: () => ({}),
  computed: {
    cart() {
      return this.$store.state.cart;
    }
  },
    methods: {
      // sendTicket() {
      //     let endpoint = "api/ticket/"
      //     let method = "POST"
      //         // const sendData: {
      //         //     "client": "user",
      //         //
      //         //     "seans_name": cart[0].seans.seans_name,
      //         // }
      // }
    }
};
</script>

<style scoped></style>
