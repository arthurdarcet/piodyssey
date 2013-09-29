Piodyssey.Views.Exam = Backbone.View.extend({
    el: '.container',
    current_question_id: 0,
    mode: 'exam',
    finnished: false,
    events: {
        'click .action-change-mode': 'click_change_mode'
    },

    initialize: function() {
        this.question = new Piodyssey.Views.Question({
            el: this.$('#exam'),
            exam: this,
            next: _.bind(function() {
                this.current_question_id++;
                this.render();
            }, this)
        });
        this.response = new Piodyssey.Views.Session({
            el: this.$('#exam')
        });
        this.response.on('go-to-question', _.bind(function(question_id) {
            this.go_to_question(this.collection.get(question_id));
        }, this));
    },

    render: function() {
        this.go_to_question(this.collection.at(this.current_question_id));
    },

    go_to_question: function(question) {
        this.finnished = _.isNaN(this.current_question_id);
        if (question) {
            this.question.set_model(question);
            this.question.render();
        }
        else {
            this.$('#exam').hide();
            this.$('#spinner').removeClass('hide');
            this.current_question_id = NaN;
            this.collection.with_session(_.bind(function(session) {
                Piodyssey.session = this.response.model = session;
                this.response.render();
                this.$('#spinner').addClass('hide');
                this.$('#exam').show();
            }, this));
        }
    },

    click_change_mode: function(evt) {
        var el = $(evt.currentTarget);
        if (el.hasClass('active')) return;
        this.mode = el.data('mode');
        this.$('.action-change-mode').toggleClass('active');
        this.render();
    }

});
