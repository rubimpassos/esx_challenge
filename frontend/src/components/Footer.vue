<template>
  <v-footer color="#333333" class="white--text" height="48">
    <div id="air" class="orange--text">
      <div class="mx-3 my-3">
        <v-icon small class="font-weight-thin orange--text">mdi-circle-slice-8</v-icon> NO AR
      </div>
    </div>
    <div class="text-uppercase body-2">
      <v-icon small class="grey--text mr-1">mdi-television</v-icon> Encontro - 10:00
    </div>
    <div class="font-italic body-2 ml-10">
      <v-icon small class="grey--text mr-1">mdi-update</v-icon> Última atualização em <strong>10:28</strong>
    </div>
    <v-spacer></v-spacer>
    <div class="justify-center">
      <span class="font-italic body-2 font-weight-thin">
        Quinta, <strong>13</strong> de <strong>Maio</strong> de <strong>2019</strong>
      </span>
      <span class="font-weight-bold title orange--text ml-3">// 10:30:42</span>
    </div>
  </v-footer>
</template>

<script>
export default {
  name: 'Footer'
}
</script>

<style scoped>
#air {
  background-color: #2c2c2c;
  width: 135px;
  clip-path: polygon(100% 100%, 100% 100%, 0% 100%, 0% 0%, 75% 0%);
  margin: -6px 50px 0 -16px;
}
</style>
