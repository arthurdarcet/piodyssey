Piodyssey.Models.Question = Backbone.Model.extend({
    parse: function(data) {
        var responses = data.responses;
        data.responses = [];
        for(var key in responses)
            data.responses.push({key: key, value: responses[key]});
        return data;
    },
    initialize: function() {
        this.on('change:answers', function() {
            this.set({user_is_right: this.get('answers') == this.get('solution')});
        });
    }
});
