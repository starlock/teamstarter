define([
    'text!template/layout/main.html',
    './layout/navigation'
], function(
    BaseMarkup,
    NavigationLayout
) {
    var ApplicationView = Backbone.View.extend({
        render: function() {
            var content = Mustache.render(BaseMarkup, {});
            this.$el.append(content);
            return this;
        }
    });

    var onDocumentReady = function() {
        var bodyNode = $('body');
        var curtainNode = $('#curtain');
        var container = $('<div/>');

        container.append(new ApplicationView().render().$el);
        container.hide();
        bodyNode.append(container);

        curtainNode.fadeOut('slow');
        container.fadeIn('slow');
    };

    // Listen to the DOMReady event
    $(onDocumentReady());
});
