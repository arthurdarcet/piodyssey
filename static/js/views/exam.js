Piodyssey.Views.Exam = Backbone.View.extend({
    el: '.container',
    current_question_id: 0,

    initialize: function() {
        this.question = new Piodyssey.Views.Question({
            el: this.$('#exam'),
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
        if (question) {
            this.question.set_model(question);
            this.question.render(_.isNaN(this.current_question_id));
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
    }
});
