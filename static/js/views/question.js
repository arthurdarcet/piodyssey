Piodyssey.Views.Question = Backbone.View.extend({
    events: {
        'click .action-next': 'click_next',
        'click .response': 'click_response'
    },

    set_model: function(model) {
        this.model = model;
        this._answer = {};
    },

    render: function(finnished) {
        var data = this.model.attributes;
        data.finnished = finnished;
        _.each(data.responses, function(response) {
            response.chosen = (data.answer || '').indexOf(response.key) >= 0;
            response.right = data.solution.indexOf(response.key) >= 0;
        });
        this.$el.html(Piodyssey.Templates.question.render(data));
    },

    answer: function() {
        var ans = this._answer;
        return _.filter(_.keys(ans).sort(), function(k) { return ans[k]; }).join('');
    },

    click_next: function() {
        this.model.set({answer: this.answer()});
        this.options.next();
    },

    click_response: function(evt) {
        var el = $(evt.currentTarget);
        el.toggleClass('active');
        this._answer[el.data('rid')] = el.hasClass('active');
    }
});
