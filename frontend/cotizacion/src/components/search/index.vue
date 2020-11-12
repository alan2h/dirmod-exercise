<template>
<div>
        <nav-bar></nav-bar>
        <br>
    <div>
            <div v-if="get_status">
                <b-card-group  deck>
                    <b-card
                        border-variant="primary"
                        header="Moneda Cotizacion"
                        header-bg-variant="primary"
                        header-text-variant="white"
                        align="center"
                    >
                        <b-card-text>{{ get_result.moneda }}</b-card-text>
                        <b-card-text>{{ get_result.precio }}</b-card-text>
                    </b-card>
                </b-card-group>
            </div>

            <div v-if="!get_status">
                <div class="alert alert-danger" role="alert">
                    Esta moneda no esta dentro del json en el backend
                </div>
            </div>
    </div>
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
    computed: mapGetters(['get_result', 'get_status']),
}
</script>