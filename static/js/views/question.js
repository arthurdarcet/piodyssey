Piodyssey.Views.Question = Backbone.View.extend({
    events: {
        'click .action-next': 'click_next',
        'click .response': 'click_response'
    },

    set_model: function(model) {
        this.model = model;
        this._answers = {};
    },

    render: function() {
        this.$el.html(Piodyssey.Templates.question.render(this.model.attributes));
    },

    answers: function() {
        var ans = this._answers;
        return _.filter(_.keys(ans).sort(), function(k) { return ans[k]; }).join('');
    },

    click_next: function() {
        this.model.set({answers: this.answers()});
        this.options.next();
    },

    click_response: function(evt) {
        var el = $(evt.currentTarget);
        el.toggleClass('active');
        this._answers[el.data('rid')] = el.hasClass('active');
    }
});
