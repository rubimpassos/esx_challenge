<template>
  <div class="user-list">
    <v-container class="my-5 px-10" fluid>
      <v-data-table
        :headers="headers"
        :items="users"
        :page.sync="page"
        :items-per-page="itemsPerPage"
        item-key="username"
        show-select
        hide-default-footer
        class="elevation-1"
        @page-count="pageCount = $event"
      >
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
      <div class="text-center pt-2">
        <v-pagination v-model="page" color="pink" depressed :length="pageCount"></v-pagination>
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
      ],
      users: [
        {
          username: 'user1',
          email: 'email1@gmail.com',
          created: '28/05/2019',
          modified: '30/05/2019',
          rules: '01',
          status: 'ATIVO'
        },
        {
          username: 'user2',
          email: 'email1@gmail.com',
          created: '28/05/2019',
          modified: '30/05/2019',
          rules: '01',
          status: 'ATIVO'
        },
        {
          username: 'user3',
          email: 'email1@gmail.com',
          created: '28/05/2019',
          modified: '30/05/2019',
          rules: '01',
          status: 'ATIVO'
        },
        {
          username: 'user4',
          email: 'email1@gmail.com',
          created: '28/05/2019',
          modified: '30/05/2019',
          rules: '01',
          status: 'ATIVO'
        },
        {
          username: 'user5',
          email: 'email1@gmail.com',
          created: '28/05/2019',
          modified: '30/05/2019',
          rules: '01',
          status: 'ATIVO'
        },
        {
          username: 'user6',
          email: 'email1@gmail.com',
          created: '28/05/2019',
          modified: '30/05/2019',
          rules: '01',
          status: 'ATIVO'
        },
        {
          username: 'user7',
          email: 'email1@gmail.com',
          created: '28/05/2019',
          modified: '30/05/2019',
          rules: '01',
          status: 'ATIVO'
        },
        {
          username: 'user8',
          email: 'email1@gmail.com',
          created: '28/05/2019',
          modified: '30/05/2019',
          rules: '01',
          status: 'ATIVO'
        },
        {
          username: 'user9',
          email: 'email1@gmail.com',
          created: '28/05/2019',
          modified: '30/05/2019',
          rules: '01',
          status: 'ATIVO'
        },
        {
          username: 'user10',
          email: 'email1@gmail.com',
          created: '28/05/2019',
          modified: '30/05/2019',
          rules: '01',
          status: 'ATIVO'
        },
        {
          username: 'user11',
          email: 'email1@gmail.com',
          created: '28/05/2019',
          modified: '30/05/2019',
          rules: '01',
          status: 'ATIVO'
        }
      ]
    }
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

.v-pagination::v-deep {
  button {
    height: 55px !important;
    min-width: 50px !important;
  }

  .v-pagination__navigation {
    width: auto;
    padding-left: 5px;
    padding-right: 5px;
  }
}
</style>
