Piodyssey.Views.Exam = Backbone.View.extend({
    el: '.container',
    current_question: 0,
    initialize: function() {
        this.question_view = new Piodyssey.Views.Question({
            el: this.$el.find('#question'),
            next: _.bind(function() {
                this.current_question++;
                this.render();
            }, this)
        });
    },
    render: function() {
        this.question_view.set_model(this.collection.at(this.current_question));
        this.question_view.render();
    }
});
