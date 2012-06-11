define([
    '../view/signup',
    'text!template/layout/navigation.html'
], function(
    SignupView,
    NavigationMarkup
) {
    var NavigationLayout = Backbone.View.extend({
        events: {
            'click #signup-link': 'onSignupClick',
        },

        render: function() {
            var content = Mustache.render(NavigationMarkup);
            this.$el.append(content);
            return this;
        },

        /************************************************************
         * EVENT CALLBACKS
         ***********************************************************/

        onSignupClick: function(e) {
            e.preventDefault();
            var signupModal = new SignupView();
            var signupModalElement = signupModal.render().$el;
            $('body').append(signupModalElement);
            signupModalElement.modal();
        }
    });
    return NavigationLayout;
});
