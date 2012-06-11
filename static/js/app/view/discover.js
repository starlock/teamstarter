define(function() {
    var DiscoverView = Backbone.View.extend({
        render: function() {
            var content = this.make('h1', {}, 'Discover view');
            this.$el.append(content);
            return this;
        }
    });
    return DiscoverView;
});
