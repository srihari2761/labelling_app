<template>
 <v-container>
  <v-layout class="temp" row wrap>
    <v-flex md6 xs12>
      <v-img class="image" :aspect-ratio="1" src="/img.png">
      </v-img>

      Wow

    </v-flex>
    <v-flex md6 xs12>
      <!--<v-layout align-space-around justify-space-around  row fill-height fill-width wrap>-->
      <!--<v-flex md12 xs4>-->
      <!--<v-btn color="success">Normal</v-btn>-->
      <!--</v-flex>-->
      <!--<v-flex md12 xs4>-->
      <!--<v-btn color="success">Success</v-btn>-->
      <!--</v-flex>-->
      <!--<v-flex md12 xs4>-->
      <!--<v-btn color="success">Success</v-btn>-->
      <!--</v-flex>-->

      <!--<v-btn color="success">Success</v-btn>-->
      <!--<v-btn color="success">Success</v-btn>-->
      <!--<v-btn color="success">Success</v-btn>-->
      <!--<v-btn color="success">Success</v-btn>-->
      <!--<v-btn color="success">Success</v-btn>-->
      <!--<v-btn color="success">Success</v-btn>-->
      <!--<v-btn color="success">Success</v-btn>-->
      <!--<v-btn color="success">Success</v-btn>-->
    <!--<v-layout align-space-around justify-space-around  row fill-height fill-width>-->
          <!--<v-btn color="success">Previous</v-btn>-->
          <!--<v-btn color="success">Mark</v-btn>-->
          <!--<v-btn color="success">Next</v-btn>-->
    <!--</v-layout>-->

      <!--</v-layout>-->

      <v-item-group>
        <v-container grid-list-md>
          <v-layout wrap>
            <v-flex
              v-for="n in 12"
              :key="n"
              xs3
              md3
            >
              <v-item>
                <v-card

                  slot-scope="{ active, toggle }"
                  :color="active ? 'primary' : ''"
                  class="d-flex align-center card-custom"
                  dark

                  @click="toggle"
                >                      
                {{Active[n]}}

                  
                </v-card>
              </v-item>
            </v-flex>
          </v-layout>
        </v-container>
      </v-item-group>

      <v-item-group>
        <v-container grid-list-md>
          <v-layout wrap>
            <v-flex
              v-for="n in 3"
              :key="n"
              xs4
              md4
            >
              <v-item>
                <v-card

                  class="d-flex align-center card-custom"
                  dark

                  @click="toggleon(Active1[n])"
                >
                    {{Active1[n]}}

                </v-card>
              </v-item>
            </v-flex>
          </v-layout>
        </v-container>
      </v-item-group>

    </v-flex>
  </v-layout> 
</v-container>
</template>

<script>
  export default {
    data: () => ({

      Active:["Saab", "Volvo", "BMW","Saab", "Volvo", "BMW","Saab", "Volvo", "BMW","Saab", "Volvo", "BMW"],
      Active1: ["chuck","Previous", "Not Sperm", "Next"],
      label: "",
      imageno:""
    }),
    methods: {
      toggleon:function(temp){

      console.log(temp)
      console.log(this.$route.params)

      }
    },
  }
</script>

<style>

  .card-custom{
    height: 100px;
  }
@media (max-width: 425px) {
.temp{
  flex-direction: column 
}
  .card-custom{
    height: 30px;
  }

.image{
  /* object-fit: cover; */
  /* max-height: 60vh; */
  /* height: 30px; */
  /* width: 30px; */
  /* width: 100v÷w; */
  }
}
.image{
  /* object-fit: cover; */
  /* max-height: 60vh; */
  /* height: 80vh; */
  /* width: 80vh; */
  /* width: 100v÷w; */
  }





</style>
