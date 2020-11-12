<template>
        <b-navbar toggleable="lg" type="dark" variant="info">
            <b-navbar-brand href="#" @click="redirectHome()">Inicio</b-navbar-brand>
            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
            <b-collapse id="nav-collapse" is-nav>
                <!-- <b-navbar-nav>
                    <b-nav-item href="#">Link</b-nav-item>
                    <b-nav-item href="#" disabled>Disabled</b-nav-item>
                </b-navbar-nav>-->
                <!-- Right aligned nav items -->
                <b-navbar-nav class="ml-auto">
                    <b-nav-form>
                        <b-form-input size="sm" class="mr-sm-2" v-model="text" placeholder="Ingresar Moneda"></b-form-input>
                        <b-button size="sm" class="my-2 my-sm-0" type="button" @click="searchText">Buscar</b-button>
                    </b-nav-form>
                   
                </b-navbar-nav>
            </b-collapse>
        </b-navbar>
</template>

<script>

import { mapActions } from 'vuex'

export default {
    data(){
        return{
            text: ''
        }
    },
    methods: {
        ...mapActions(['set_result']),
        redirectHome(){
            this.$router.push({path: '/'})
        },
        searchText(){
            this.set_result(this.text)
            if (this.$route.path !== '/search') {
                this.$router.push({name: 'search'})
            }
            
        }
    }
}
</script>