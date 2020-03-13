<template>
  <nav>
    <v-app-bar height="87" class="lighten-5">
      <v-btn class="main-btn gradient-btn white mx-3 py-4" min-width="45px">
        <v-icon color="white">mdi-google-podcast</v-icon>
      </v-btn>

      <v-divider class="mx-4" inset vertical></v-divider>

      <v-btn-toggle
        v-model="toggle_exclusive"
        mandatory
        borderless
        class="elevation-3"
      >
        <v-btn class="white pa-4">
          <v-icon>mdi-security</v-icon>
        </v-btn>

        <v-btn class="white pa-4">
          <v-icon>mdi-account</v-icon>
        </v-btn>
      </v-btn-toggle>

      <v-row
        class="align-self-end"
        style="max-width: 450px"
      >
        <v-text-field
          label="Pesquisar..."
          class="ml-10 mx-3 font-italic"
          single-line
          append-icon="mdi-magnify"
          color="pink"
        />
      </v-row>

      <v-spacer></v-spacer>

      <v-btn min-width="0" elevation="3" class="white mr-3 px-3 py-6">
        <v-icon light>mdi-tune</v-icon>
      </v-btn>

      <v-btn depressed class="pink white--text darken-1 px-5 py-6">
        <v-icon light left>mdi-account</v-icon>
        <span class="font-weight-regular">Incluir Usuário</span>
      </v-btn>

      <v-divider class="mx-4" inset vertical></v-divider>

      <v-btn icon class="pl-0 ml-0">
        <v-icon>mdi-home</v-icon>
      </v-btn>
      <v-btn icon>
        <v-icon>mdi-cog</v-icon>
      </v-btn>
      <v-btn icon>
        <v-icon>mdi-power</v-icon>
      </v-btn>
    </v-app-bar>
  </nav>
</template>

<script>
export default {
  name: 'Navbar',
  data () {
    return {
      toggle_exclusive: 1
    }
  }
}
</script>

<style lang="scss" scoped>
.main-btn {
  width: 48px;
  border-radius: 60% 60% 60% 60% / 25% 25% 25% 25%;
}

.gradient-btn {
  background: linear-gradient(27deg, rgb(186, 53, 111) 0%, rgb(253, 96, 29) 61%, rgb(253, 149, 29) 100%);
  i {
    color: white;
  }
}

.v-item--active {
  background: linear-gradient(27deg, rgb(186, 53, 111) 0%, rgb(253, 96, 29) 61%, rgb(253, 149, 29) 100%);
  border-radius: 5px !important;
  i {
    color: white !important;
  }
}

%smooth-line {
  border-radius: 100px;
  border-color: rgba(0, 0, 0, 0.09) !important;
  border-width: 1px !important;
}

.v-input::v-deep .v-input__slot::before {
  @extend %smooth-line
}

.v-divider--vertical {
  height: 25px;
  align-self: center;
  @extend %smooth-line
}

.v-btn:not(.v-btn--flat):before {
  display: none;
}
</style>
