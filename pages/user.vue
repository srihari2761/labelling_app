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
                  <v-scroll-y-transition>
                    <div
                      v-if="active"
                      class="display-3 text-xs-center"
                    >
                      Active
                    </div>
                  </v-scroll-y-transition>
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

                  slot-scope="{ active, toggle }"
                  :color="active ? 'primary' : ''"
                  class="d-flex align-center card-custom"
                  dark

                  @click="toggle"
                >
                  <v-scroll-y-transition>
                    <div
                      v-if="active"
                      class="display-3 text-xs-center"
                    >
                      Active
                    </div>
                  </v-scroll-y-transition>
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

// console.log(this.$route.user)
// console.log(this.$route.query.user)
// console.log(this.$route.params)


  export default {
    data: () => ({
      ecosystem: [
        {
          text: 'vuetify-loader',
          href: 'https://github.com/vuetifyjs/vuetify-loader'
        },
        {
          text: 'github',
          href: 'https://github.com/vuetifyjs/vuetify'
        },
        {
          text: 'awesome-vuetify',
          href: 'https://github.com/vuetifyjs/awesome-vuetify'
        }
      ],
      importantLinks: [
        {
          text: 'Documentation',
          href: 'https://vuetifyjs.com'
        },
        {
          text: 'Chat',
          href: 'https://community.vuetifyjs.com'
        },
        {
          text: 'Made with Vuetify',
          href: 'https://madewithvuetifyjs.com'
        },
        {
          text: 'Twitter',
          href: 'https://twitter.com/vuetifyjs'
        },
        {
          text: 'Articles',
          href: 'https://medium.com/vuetify'
        }
      ],
      whatsNext: [
        {
          text: 'Explore components',
          href: 'https://vuetifyjs.com/components/api-explorer'
        },
        {
          text: 'Select a layout',
          href: 'https://vuetifyjs.com/layout/pre-defined'
        },
        {
          text: 'Frequently Asked Questions',
          href: 'https://vuetifyjs.com/getting-started/frequently-asked-questions'
        }

      ]
    })
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

/* .image{
  object-fit: cover;
  max-height: 60vh;
  height: 30px;
  width: 30px;
  width: 100v÷w;
  }
}
.image{
  object-fit: cover;
  max-height: 60vh;
  height: 80vh;
  width: 80vh;
  width: 100v÷w;
  }

 */

}

</style>
