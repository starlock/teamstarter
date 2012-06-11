define([
    'text!template/layout/main.html',
    './layout/navigation'
], function(
    BaseMarkup,
    NavigationLayout
) {
    var app = {};

    var ApplicationView = Backbone.View.extend({
        render: function() {
            var content = Mustache.render(BaseMarkup, {});
            this.$el.append(content);
            this.renderNavigation();
            return this;
        },

        events: {
            'click #login-btn': 'onLoginClick',
        },

        onLoginClick: function(e) {
            e.preventDefault();
            var email = $('#login-email').val();
            var password = $('#login-password').val();

            if (email && password) {
                var AuthUser = Backbone.Model.extend({urlRoot : '/api/user/auth'});
                var auth = new AuthUser({
                    'email': email,
                    'password': password
                });

                auth.save(null, {
                    success: function(e) {
                        console.log('Logged in');
                        console.log(e);
                    },
                    error: function() {
                        console.log('Failed to login');
                    },
                });
            }
        },

        renderNavigation: function() {
            var navigation = new NavigationLayout();
            if (_.isUndefined(this.currentNavigation) !== true) {
                this.currentNavigation.remove();
            }

            this.currentNavigation = navigation;
            this.$('#nav-container').append(navigation.render().$el);
            return this;
        },
    });

    var onDocumentReady = function() {
        var bodyNode = $('body');
        var container = $('<div/>');
        var curtainNode = $('#curtain');

        // Render application view
        var view = app.view = new ApplicationView();
        container.append(view.render().$el);

        // Prepare application view for coming effects
        container.hide();
        bodyNode.append(container);

        // Swap curtain against prepared application DOM
        curtainNode.fadeOut(1000);
        container.fadeIn(1000);
    };

    // Listen to the DOMReady event
    $(onDocumentReady());
});
