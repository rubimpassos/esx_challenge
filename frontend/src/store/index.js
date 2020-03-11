import Vue from 'vue'
import Vuex from 'vuex'
import client from 'api-client'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    users: []
  },
  mutations: {
    setUsers (state, users) {
      state.users = users
    }
  },
  actions: {
    fetchUsers ({ commit }) {
      return client.fetchUsers().then(users => commit('setUsers', users))
    }
  },
  modules: {
  }
})
