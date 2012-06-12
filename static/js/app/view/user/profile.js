define(function() {
    var UserProfileView = Backbone.View.extend({
        render: function() {
            var content = this.make('h1', {}, 'Hello user profile view');
            this.$el.append(content);
            return this;
        }
    });
    return UserProfileView;
});
