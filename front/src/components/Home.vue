<template lang="html">
   
    <div>
        <div class="container tabla">
            <div class="row">
                <div class="col-md-12">
                    <p class="text-center">Loremzsiohf shiso sojpdgos goi</p>
                    <div>
                        <h1>Flask Google Maps Example</h1>
                        <p>{{ riders }}</p>      
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Main',
    data(){
        return{
            riders: '',
            prueba: '',
            lista:''
        }
    },
    methods: {
        getRiders(){
            const path = 'http://localhost:8000/sendjson/'
            axios.get(path).then((response) =>{
                this.riders = response.data

               
            })
            .catch((error) =>{
                console.log(error);
            })
        }
    },
    created(){
        this.getRiders();
        
        
    }
    
    
}
</script>

<style lang="css" scoped>

.tabla{
    border: 1px solid black;
    }

</style>


