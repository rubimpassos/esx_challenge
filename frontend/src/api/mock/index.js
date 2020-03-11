import users from './data/users'

const fetch = (mockData, time = 0) => {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(mockData)
    }, time)
  })
}

export default {
  fetchUsers () {
    return fetch(users, 1000) // wait 1s before returning posts
  }
}
