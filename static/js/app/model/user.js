define(function() {
    var Model = Backbone.Model.extend({
        url: function() {
            return this.id ? '/api/user/' + this.id : '/api/user/create';
        }
    });
    return Model;
});
