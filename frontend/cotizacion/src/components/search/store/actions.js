
import axios from 'axios';

export const set_result = ({commit}, payload) => {
    axios.get(`/cotizacion/${payload}/`)
    .then(response => {
        commit('set_result', response.data)
        commit('set_status', true)
    }).catch(error => {
        commit('set_result', {})
        commit('set_status', false)
        console.log(error)
    })
}