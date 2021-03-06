Piodyssey.Views.Session = Backbone.View.extend({
    events: {
        'click .action-go-to-question': 'go_to_question'
    },

    render: function() {
        var data = this.model.attributes;
        data.nb_errors = _.filter(data.answers, function(a) { return !a.is_right; }).length;
        data.nb_questions = data.answers.length;
        if (data.nb_errors/data.nb_questions <= 3/35)
            data.success = 'success';
        else if (data.nb_errors/data.nb_questions <= 5/35)
            data.success = 'warning';
        else
            data.success = 'danger';
        this.$el.html(Piodyssey.Templates.session.render(this.model.attributes));
    },

    go_to_question: function(evt) {
        this.trigger('go-to-question', $(evt.currentTarget).data('qid'));
    }
});
