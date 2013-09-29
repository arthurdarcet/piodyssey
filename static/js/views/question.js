Piodyssey.Views.Question = Backbone.View.extend({
    events: {
        'click .action-correction': 'click_correction',
        'click .action-next': 'click_next',
        'click .response': 'click_response'
    },

    set_model: function(model) {
        this.model = model;
        this._answer = {};
    },

    render: function(correction) {
        var data = this.model.attributes;
        data.finnished = this.options.exam.finnished;
        data.correction = correction || data.finnished;
        data.training = this.options.exam.mode == 'training';
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

    click_correction: function() {
        this.model.set({answer: this.answer()});
        this.render(true);
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
