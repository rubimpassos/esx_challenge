<template>
  <div class="user-list">
    <v-container class="my-5 px-10" fluid>
      <v-data-table
        :headers="headers"
        :items="users"
        :page.sync="page"
        :items-per-page="itemsPerPage"
        :loading="loading"
        item-key="username"
        class="elevation-1"
        show-select
        hide-default-footer
        @page-count="pageCount = $event"
      >
        <template v-slot:item.status="{ item }">
          <div :class="[item.status === 'ATIVO' ? 'green--text' : 'red--text', 'font-weight-bold']">{{ item.status }}</div>
        </template>
        <template v-slot:item.action>
          <div class="action-buttons">
            <v-icon class="mx-2">mdi-delete</v-icon>
            <v-icon class="mx-2">mdi-package-down</v-icon>
            <v-icon class="mx-2">mdi-security</v-icon>
            <v-icon class="mx-2">mdi-pencil</v-icon>
          </div>
          <v-icon class="mx-2">mdi-dots-horizontal</v-icon>
        </template>
      </v-data-table>
      <div id="pagination" class="d-inline-flex pa-5">
        <div class="flex text-right align-self-center">
          <v-btn :disabled="page === 1" @click="page = 1">Primeira</v-btn>
        </div>
        <v-pagination v-model="page" depressed :length="pageCount"></v-pagination>
        <div class="flex text-left align-self-center">
          <v-btn :disabled="page === pageCount" @click="page = pageCount">Última</v-btn>
        </div>
      </div>
    </v-container>
  </div>
</template>

<script>
export default {
  name: 'UserList',
  data () {
    return {
      page: 1,
      pageCount: 0,
      itemsPerPage: 10,
      singleSelect: true,
      loading: false,
      selected: [],
      headers: [
        {
          text: 'USUÁRIO',
          value: 'username',
          align: 'start',
          sortable: false
        },
        {
          text: 'EMAIL',
          value: 'email',
          align: 'start',
          sortable: false
        },
        {
          text: 'DATA DE INCLUSÃO',
          value: 'created',
          align: 'start',
          sortable: false
        },
        {
          text: 'DATA DE ALTERAÇÃO',
          value: 'modified',
          align: 'start',
          sortable: false
        },
        {
          text: 'REGRAS',
          value: 'rules',
          align: 'start',
          sortable: false
        },
        {
          text: 'STATUS',
          value: 'status',
          align: 'start',
          sortable: false
        },
        {
          text: 'AÇÕES',
          value: 'action',
          align: 'end',
          sortable: false
        }
      ]
    }
  },
  computed: {
    users () {
      return this.$store.state.users
    }
  },
  created () {
    this.loading = true
    this.$store.dispatch('fetchUsers')
      .then(posts => {
        this.loading = false
      })
  }
}
</script>

<style lang="scss" scoped>
.action-buttons{
  display: none;
}

%table-border-radius{
  border-radius: 7px !important;
}

.v-data-table::v-deep {
  @extend %table-border-radius;

  .v-data-table__wrapper, table{
    @extend %table-border-radius;
  }

  thead{
    z-index: 9999;
    position: relative;
    box-shadow: 0 -5px 15px 0 rgb(181, 181, 181);

    th .v-simple-checkbox{
      display: none;
    }
  }

  .v-simple-checkbox i{
    color: rgba(0, 0, 0, 0.25);
  }

  tbody tr{

    &:nth-child(odd){
      background-color: #fafafa !important;
    }

    &:nth-child(even){
      background-color: #efefef !important;
    }

    &:last-child{
      @extend %table-border-radius;
    }

    &:hover{
      background-color: white !important;

      td{
        border-bottom: 2px solid #d81b60 !important;
      }

      .action-buttons{
        display: inline-flex;
      }
    }

    td:last-child{
      width: 240px;
    }
  }
}

#pagination::v-deep{
  width: 100%;

  button {
    height: 55px !important;
    min-width: 50px !important;
    background-color: #f5f5f5 !important;
    border: 2px solid #fafafa;
    box-shadow: none !important;

    text-transform: none !important;
    font-weight: normal !important;
    font-size: 15px;
    letter-spacing: 1.25px;
    color: grey;

    &.v-pagination__navigation {
      padding: 27px 15px;
    }

    &:disabled, &.v-pagination__navigation--disabled {
      background-color: #fafafa !important;
      color: #bbbbbb;
      padding: 27px 15px;
      opacity: 1 !important;
    }
  }

  .v-pagination {
    max-width: max-content;

    .v-pagination__item--active {
      background-color: #d81b60 !important;
      color: white;
      border: none;
    }

    li{
      i {
        display: none;
      }

      .v-pagination__navigation {
        width: auto !important;
      }

      &:first-child .v-pagination__navigation:before{
        content: 'Anterior';
      }

      &:last-child .v-pagination__navigation:before{
        content: 'Próximo';
      }
    }
  }
}
</style>
