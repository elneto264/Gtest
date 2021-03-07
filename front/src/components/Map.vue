<template>
    <div>
        <div class="container-fluid">

            <div class="row">
                <div class=" tope col-xs-12 col-md-12 col-lg-12">
                    <nav class="navbar navbar-dark bg-dark">
                        <span class="navbar-brand h1">Prueba live map</span>
                    </nav>
                </div>
            </div>

        </div>
        <div class="container">
            
            <div class="row">
                <div class="titulosC col-xs-12 col-md-6 col-lg-6">

                    <div>
                        <h2>Mis Coordenadas</h2>
                        <p>{{ myCoord.lat}} lat, {{ myCoord.lng}} lon </p>
                    </div>

                </div>
                <div class="titulosC col-xs-12 col-md-6 col-lg-6">

                    <div>
                        <h2>Coordenadas del Mapa</h2>
                        <p>{{ mapCoord.lat}} lat, {{ mapCoord.lng}} lon </p>
                    </div>

                </div>
                
            </div>
            <div class="row">

                <div class="mapCont col-xs-12 col-md-12 col-lg-12">
                    <gmap-map
                        class="gmapa"
                        :center="myCoord"
                        :zoom="zoom"
                        :options="options"
                        style="width:100%; height:660px; "
                        ref="mapRef"
                        @dragend="handDrag"
                
                    >


                        <gmap-marker :key="index"
                            v-for="(m, index) in markers"
                            :clickable="true"
                            :draggable="true"
                            :position="{lat: m.fields.lat, lng: m.fields.lng}"
                            @click="toggleInfoWindow(m, index);"
                            
                        />
                        
                         <gmap-info-window 
                                :position="infoWindowPos"
                                :opened="infoWinOpen" 
                                @closeclick="infoWinOpen=false"
                                :options="{
                                    pixelOffset: {
                                        width: 0,
                                        height: -35
                                    }
                                }"
                                ><div v-html="infoContent"></div>

                        </gmap-info-window>

                    
                    

                       


                    </gmap-map> 
                </div>

            </div>
            

            
        </div>
    </div>

</template>

<script>
import Vue from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios)

export default {
    data (){
        return{
            map:null,
            myCoord:{
                lat:0,
                lng:0
            },
            zoom:4,
            markers:[
                

            ],
            options: {
                zoomControl: true, 
                mapTypeControl: true, 
                scaleControl: true, 
                streetViewControl: true, 
                fullscreenControl: true 
            },
            infoContent:'',
            infoWindowPos: {lat: 0, lng: 0},
            infoWinOpen: false
            
        }
    },
    created(){

        if(localStorage.center){
            this.myCoord = JSON.parse(localStorage.center);
        } else {
            this.$getLocation({})
            .then(coord => {
                this.myCoord = coord;
            })
            .catch(error => alert(error));
        }

        if(localStorage.zoom) {
            this.zoom = parseInt(localStorage.zoom);
        }

    },
    
    mounted(){
        
        this.$refs.mapRef.$mapPromise.then(map => this.map = map);
            axios.get('http://localhost:8000/sendsql/').then((response) =>{
                this.markers = response.data
                
                this.markers.forEach(function(marker){
                    console.log(marker);

                   

                }) 

            })
            .catch((error) =>{
                console.log(error);
            })
            
        },
    methods: {
        toggleInfoWindow: function (marker, idx) {
        this.infoWindowPos = {lat: marker.fields.lat, lng: marker.fields.lng};
        console.log(marker);
        this.infoContent = this.getInfoWindowContent(marker);
        


        if (this.currentMidx == idx) {
          this.infoWinOpen = !this.infoWinOpen;
        }

        else {
          this.infoWinOpen = true;
          this.currentMidx = idx;
        }
      },
      getInfoWindowContent: function (marker) {
        return (
            `<div >
                    <h6 id="infoWindow">Rider</h6>
                    <ul class="list-group">
                        <li class="list-group-item"><span>ID:</span> ${marker.pk}</li>
                        <li class="list-group-item"><span>Name:</span> ${marker.fields.name}</li>
                        <li class="list-group-item"><span>Latitud:</span> ${marker.fields.lat}</li>
                        <li class="list-group-item"><span>Longitud:</span> ${marker.fields.lng}</li>
                        <li class="list-group-item"><span>transport:</span> ${marker.fields.transport}</li>
                        <li class="list-group-item"><span>autoassignmentenabled:</span> ${marker.fields.autoassignmentenabled}</li>
                        <li class="list-group-item"><span>numberoforders:</span> ${marker.fields.numberoforders}</li>
                        <li class="list-group-item"><span>mcd:</span> ${marker.fields.mcd}</li>
                        <li class="list-group-item"><span>mcc:</span> ${marker.fields.mcc}</li>
                        <li class="list-group-item"><span>checkedin:</span> ${marker.fields.checkedin}</li>
                    </ul>
            </div>`

        )
      },
        handDrag(){
            let center = {
                lat: this.map.getCenter().lat(),
                lng: this.map.getCenter().lng()
            };
            let zoom = this.map.getZoom();

            localStorage.center = JSON.stringify(center);
            localStorage.zoom = zoom;
        },
        getPosition(m){
            return {
                lat: parseFloat(m.lat),
                lng: parseFloat(m.lng)
                
                }
        }

    },
    computed:{
        mapCoord() {
            if(!this.map){

                return {
                    lat:0,
                    lng:0
                }
            }

            return {

                lat:this.map.getCenter().lat().toFixed(4),
                lng:this.map.getCenter().lng().toFixed(4)
            }
            

        }
        
    }

}
</script>

<style>
.list-group span{
    font-weight: bold;
}
.titulosC{
    padding: 0;
    margin-top: 10px;
    margin-bottom: 10px;
}
.tope{
    top:0;
    padding:0;
    
}
.gmapa{
    border: 1px solid black;
     
    
}



</style>
