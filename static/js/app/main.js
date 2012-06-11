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
        var bodyNode = $('body'),
            curtainNode = $('#curtain'),
            container = $('<div/>');


        container.append(new ApplicationView().render().$el);
        curtainNode.fadeOut('slow', function() {
            bodyNode.append(container.contents());
        });
    };

    $(function() {
        onDocumentReady();
    });
});
