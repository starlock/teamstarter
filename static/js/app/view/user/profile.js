define(['text!template/layout/user/profile.html'],
function(UserProfileMarkup) {
    var UserProfileView = Backbone.View.extend({
        events: {
            'click #user-save-btn': 'onUserProfileClick'
        },

        onUserProfileClick: function(e) {
            e.preventDefault();
            console.log('onUserProfileClick');
        },

        render: function() {
            var params = {};
            params.user = window.session.attributes;
            var content = Mustache.render(UserProfileMarkup, params);
            this.$el.append(content);
            return this;
        }
    });
    return UserProfileView;
});
