Piodyssey.Collections.Questions = Backbone.Collection.extend({
    model: Piodyssey.Models.Question,
    _loading_session: false,

    with_session: function(cb) {
        if (Piodyssey.session) return cb(Piodyssey.session);
        if (this._loading_session) return false;
        this._loading_session = true;
        $.post(
            '/api/session',
            {
                'answers': JSON.stringify(this.map(function(question) {
                    return [question.id, question.get('answer') || ''];
                }))
            }
        ).done(_.bind(function(data) {
            cb(Piodyssey.session = new Piodyssey.Models.Session(data, {parse: true}));
        }, this)).always(_.bind(function() {
            this._loading_session = false;
        }, this));
    }
});
