define(function() {
    var ProjectCreateView = Backbone.View.extend({
        render: function() {
            var content = this.make('h1', {}, 'Hello project create');
            this.$el.append(content);
            return this;
        }
    });
    return ProjectCreateView;
});
