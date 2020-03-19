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

      <v-btn min-width="0" elevation="3" class="white mr-3 px-3 py-6" @click.stop="drawer = !drawer">
        <v-icon light>mdi-tune</v-icon>
      </v-btn>

      <v-btn color="primary" depressed class="px-5 py-6">
        <v-icon left>mdi-account</v-icon>
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
    <v-navigation-drawer
      v-model="drawer"
      color="grey"
      class="lighten-3"
      width="400"
      absolute
      temporary
      right
    >
      <v-sheet color="white" class="py-7 pl-7 pr-2" tile>
        <h2 class="font-weight-thin text-uppercase d-inline">
          <v-icon>mdi-tune</v-icon>
          Filtros
        </h2>
        <v-btn right min-width="0" elevation="3" class="white mr-3 px-3 py-6 float-right"
               @click.stop="drawer = !drawer">
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </v-sheet>

      <v-container fluid>
        <p class="font-italic body-2">
          Utilize os filtros abaixo para refinar os resultados da tabela, clique no botão APLICAR  para salvar as alterações
        </p>
        <v-divider style="width: 32px; border-width: thin"></v-divider>
        <v-form class="py-5">
          <v-row align="center">
            <v-col class="d-flex py-2">
              <v-menu
                ref="created_menu"
                v-model="created_menu"
                :close-on-content-click="false"
                :return-value.sync="created_filter"
                transition="scale-transition"
                offset-y
                min-width="290px"
              >
                <template v-slot:activator="{ on }">
                  <v-text-field
                    v-model="created_filter"
                    label="TODAS AS DATAS DE INCLUSÃO"
                    prepend-inner-icon="mdi-calendar-range"
                    append-icon="mdi-menu-down"
                    readonly
                    clearable
                    v-on="on"
                    @click:clear="created_filter = null"
                  ></v-text-field>
                </template>
                <v-date-picker v-model="created_filter" no-title scrollable>
                  <v-spacer></v-spacer>
                  <v-btn text color="primary" @click="created_menu = false">Cancel</v-btn>
                  <v-btn text color="primary" @click="$refs.created_menu.save(created_filter)">OK</v-btn>
                </v-date-picker>
              </v-menu>
            </v-col>
          </v-row>
          <v-row align="center">
            <v-col class="d-flex py-2">
              <v-menu
                ref="modified_menu"
                v-model="modified_menu"
                :close-on-content-click="false"
                :return-value.sync="modified_filter"
                transition="scale-transition"
                offset-y
                min-width="290px"
              >
                <template v-slot:activator="{ on }">
                  <v-text-field
                    v-model="modified_filter"
                    label="TODAS AS DATAS DE ALTERAÇÃO"
                    prepend-inner-icon="mdi-calendar-range"
                    append-icon="mdi-menu-down"
                    readonly
                    clearable
                    v-on="on"
                    @click:clear="modified_filter = null"
                  ></v-text-field>
                </template>
                <v-date-picker v-model="modified_filter" no-title scrollable>
                  <v-spacer></v-spacer>
                  <v-btn text color="primary" @click="modified_menu = false">Cancel</v-btn>
                  <v-btn text color="primary" @click="$refs.modified_menu.save(modified_filter)">OK</v-btn>
                </v-date-picker>
              </v-menu>
            </v-col>
          </v-row>
          <v-row align="center">
            <v-col class="d-flex py-2">
              <v-select
                v-model="status_filter"
                label="ATIVOS E INATIVOS"
                prepend-inner-icon="mdi-circle-medium"
                color="primary"
                :items="status"
                clearable
                @click:clear="status_filter = null"
              ></v-select>
            </v-col>
          </v-row>

          <v-btn color="primary" class="py-6" block outlined>APLICAR</v-btn>
        </v-form>
      </v-container>
    </v-navigation-drawer>
  </nav>
</template>

<script>
export default {
  name: 'Navbar',
  data () {
    return {
      toggle_exclusive: 1,
      drawer: null,
      created_menu: false,
      created_filter: null,
      modified_menu: false,
      modified_filter: null,
      status_filter: null,
      status: [
        { text: 'Ativo', value: 'active' },
        { text: 'Inativo', value: 'inactive' }
      ]
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

.v-input::v-deep .v-label{
  color: var(--v-primary-base);
  font-weight: 400;
}
</style>
