new Vue({
    el: '.base',
    delimiters: ["[[", "]]"],
    vuetify: new Vuetify(),
    data: () => ({
        links: [
          'Home',
          'About Us',
          'Team',
          'Services',
          'Blog',
          'Contact Us',
        ],
        videos_all: [],
        videos: [],
        category: 'all'
      }),
      created() {
        this.initialize()
      },
      watch: {
        category() {
          if (this.category == 'all') {
            this.videos = this.videos_all
          }
          else if(this.category == 'people') {
            this.videos = this.videos_all.filter(function(element) {
              return element.category == "Ludzie"
            })
          }
          else if(this.category == 'sport') {
            this.videos = this.videos_all.filter(function(element) {
              return element.category == "Sport"
            })
          }
          else if(this.category == 'dance') {
            this.videos = this.videos_all.filter(function(element) {
              return element.category == "Taniec"
            })
          }
          else if(this.category == 'animals') {
            this.videos = this.videos_all.filter(function(element) {
              return element.category == "Zwierzęta"
            })
          }
          else if(this.category == 'others') {
            this.videos = this.videos_all.filter(function(element) {
              return element.category == "Inne"
            })
          }
        }
      },
      methods: {
        initialize() {
          this.getVideos()
        },
        getVideos() {
          self = this
            return $.ajax({
                'url': '/miniplayer/getVideos',
                'type': 'GET',
                'dataType': 'JSON',
            })
            .done( function (response) {
                self.videos_all = response
                self.videos = self.videos_all
            })
        },
        changeCategory(category)
        {
          this.category = category
        },
        openVideo(video) {
          window.location.pathname = 'miniplayer/video/' + video.id
        },
        home() {
          window.location.reload()
        },
        logout() {
            window.location.pathname = "/logout"
        }
      }
  })