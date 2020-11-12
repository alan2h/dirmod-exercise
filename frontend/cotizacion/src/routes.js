import home from './components/home'
import search from './components/search'
import errorPage from './components/404'

export const routes = [
    { path: '/', component: home },
    { path: '/search/', component: search, name:'search' },
    { path: "*", component: errorPage }
  ]