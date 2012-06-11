define([
    '../view/signup',
    'text!template/layout/navigation.html',
    'app/util'
], function(
    SignupView,
    NavigationMarkup,
    Utility
) {
    var NavigationLayout = Backbone.View.extend({
        events: {
            'click #signup-link': 'onSignupClick',
            'click a': 'onNavigationClick',
        },

        render: function() {
            var params = {};

            if (typeof window.session !== 'undefined') {
                params.is_authenticated = true;
                params.user = {};
                params.user.email = window.session.get('email');
            }

            var content = Mustache.render(NavigationMarkup, params);
            this.$el.append(content);
            return this;
        },

        /************************************************************
         * EVENT CALLBACKS
         ***********************************************************/

        onNavigationClick: function(e) {
            var node = $(e.currentTarget);
            var link = node.attr('href');

            /*
             * In case the URL in the anchor is # or begins
             * with // or http then we abort manual handling (highjacking)
             * since we should treat it normally by design.
             */
            if (link === '#' ||
                link.slice(0, 2) === '//' ||
                link.slice(0, 4) === 'http')
            {
                return;
            }

            e.preventDefault();
            Utility.Mediator.trigger('page:navigate', link);
        },

        onSignupClick: function(e) {
            e.stopPropagation();
            e.preventDefault();

            var signupModal = new SignupView();
            var signupModalElement = signupModal.render().$el;
            $('body').append(signupModalElement);
            signupModalElement.modal();
        }
    });
    return NavigationLayout;
});
