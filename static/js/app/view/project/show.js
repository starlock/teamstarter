define(function() {
    var ShowProjectView = Backbone.View.extend({
        render: function() {
            var content = this.make('h1', {}, 'Hello show project view');
            this.$el.append(content);
            return this;
        }
    });
    return ShowProjectView;
});
