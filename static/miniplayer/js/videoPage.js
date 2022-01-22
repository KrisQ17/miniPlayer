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
        video_id: 0,
        video: null,
        rating: 0,
        comment: "",
        comments: []
      }),
    created() {
        this.initialize()
    },
    watch: {
        rating() {
            this.setRating(this.rating)
        }
    },
    methods: {
        initialize() {
            this.video_id = window.location.pathname.split('/')[3]
            this.getVideo()
            this.getRating()
            this.getComments()
        },
        home() {
            window.location.pathname = 'miniplayer'
        },
        getVideo() {
            self = this
            return $.ajax({
                'url': '/miniplayer/video/' + self.video_id,
                'type': 'POST',
                'data': {
                    type: "video",
                    csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
                },
                'dataType': 'JSON',
            })
            .done( function (response) {
                self.video = response
                self.video.path = '/' + self.video.path
            })
        },
        getRating() {
            self = this
            return $.ajax({
                'url': '/miniplayer/video/' + self.video_id + '/rating',
                'type': 'GET',
                'data': {
                    type: "videoStat",
                    csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
                },
                'dataType': 'JSON',
            })
            .done( function (response) {
                self.rating = response['rating']
            })
        },
        setRating() {
            self = this
            return $.ajax({
                'url': '/miniplayer/video/' + self.video_id + '/rating',
                'type': 'POST',
                'data': {
                    rating: self.rating,
                    csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
                },
                'dataType': 'JSON',
            })
            .done( function (response) {
                if (response == 1) {
                    self.getRating()
                }
            })
        },
        getComments() {
            self = this
            return $.ajax({
                'url': '/miniplayer/video/' + self.video_id + '/comments',
                'type': 'GET',
                'dataType': 'JSON',
            })
            .done( function (response) {
                self.comments = response
            })
        },
        addComment() {
            self = this
            return $.ajax({
                'url': '/miniplayer/video/' + self.video_id + '/comments',
                'type': 'POST',
                'data': {
                    comment: self.comment,
                    csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
                },
                'dataType': 'JSON',
            })
            .done( function (response) {
                if(response == 1)
                {
                    self.comment = ""
                    self.getComments()
                }
            })
        },
        correctDate (date) {
            let dateVisit = dayjs(date, 'YYYY-MM-DDTHH:mm:ss')
            return dateVisit.format("DD.MM.YYYY HH:mm:ss")
        },
        logout() {
            window.location.pathname = "/logout"
        }
    }
})