<template>
    <div>
        <nav-bar></nav-bar>
        <table class="table">
        <thead>
            <tr>
            <th scope="col">Moneda</th>
            <th scope="col">Precio</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="history in get_history_search"  :key="history.moneda">
                <td>{{ history.moneda }}</td>
                <td>{{ history.precio }}</td>
            </tr>
        </tbody>
        </table>
    </div>
</template>

<script>

import navBar from '../shared/navBar';

import {mapGetters} from 'vuex';

export default {
    data(){
        return{

        }
    },
    components: {
        navBar
    },
    computed: mapGetters(['get_history_search'])
}
</script>