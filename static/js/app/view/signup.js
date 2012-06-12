define([
    'text!template/view/signup.html',
    'app/util',
    'model/user'
], function(SignupMarkup, utility, User) {
    var SignupView = Backbone.View.extend({
        className: 'modal hide fade',

        events: {
            'click #signup-btn': 'onCreateClick'
        },

        model: User,

        initialize: function(options) {
            SignupView.__super__.initialize.call(this, options);
            this.lazyChildren = {};
            return this;
        },

        render: function() {
            var content = Mustache.render(SignupMarkup);
            this.$el.append(content);
            return this;
        },

        getLazyChild: function(selector) {
            var current = this.lazyChildren[selector];
            if (_.isUndefined(current) !== true) {
                return current;
            }

            var child = this.$(selector);
            if (_.isNull(child)) {
                return undefined;
            }

            this.lazyChildren[selector] = child;
            return child;
        },

        getEmailField: function() {
            return this.getLazyChild('#email');
        },

        getPasswordField: function() {
            return this.getLazyChild('#password');
        },

        getPasswordRepeatField: function() {
            return this.getLazyChild('#password-repeat');
        },

        getFormData: function() {
            return {
                'email': this.getEmailField().val(),
                'password': this.getPasswordField().val(),
                'password-repeat': this.getPasswordRepeatField().val()
            };
        },

        isValidEmail: function() {
            var check = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
            if (check.test(this.getEmailField().val()) === true) {
                return true;
            }
            return false;
        },

        isValidPassword: function() {
            var chosenPassword = this.getPasswordField().val();
            if (chosenPassword.length >= 6) {
                return true;
            }
            return false;
        },

        isValidPasswordRepeat: function() {
            var chosenPassword = this.getPasswordField().val();
            var repeatedPassword = this.getPasswordRepeatField().val();
            if (repeatedPassword === chosenPassword) {
                return true;
            }
            return false;
        },

        validateForm: function() {
            var ret = true;
            this.clearPreviousErrors();
            if (this.isValidEmail() !== true) {
                this.setEmailError();
                ret = false;
            }

            if (this.isValidPassword() !== true) {
                this.setPasswordError();
                ret = false;
            }

            if (this.isValidPasswordRepeat() !== true) {
                this.setPasswordRepeatError();
                ret = false;
            }
            return ret;
        },

        saveForm: function() {
            var form = this.getFormData();
            var self = this;
            this.model = new User({'email': form.email,
                             'password': form.password});
            this.model.save(null, {
                success: function(model, response) {
                    $('.modal').modal('hide'); // self.$el doesn't work..
                    utility.Mediator.trigger('page:navigate', '/user/' + model.id);
                },
                error: function(model, response) {
                    self.setFieldError(self.getEmailField(), response.responseText);
                }});
        },



        /************************************************************
         * ERROR OUTPUT
         ***********************************************************/

        clearPreviousErrors: function() {
            $('.control-group').removeClass('error');
            $('.no-tip').each(function(index, node) {
                // P-tags contain error messages
                $('p', $(node)).remove();
            });
        },

        setEmailError: function() {
            this.setFieldError(this.getEmailField(), 'Invalid e-mail address given');
        },

        setPasswordError: function() {
            this.setFieldError(this.getPasswordField());
        },

        setPasswordRepeatError: function() {
            this.setFieldError(this.getPasswordRepeatField(), 'Does not match given password');
        },

        setFieldError: function(field, message) {
            var fieldContainer = field.parent();
            var fieldSuperContainer = fieldContainer.parent();

            fieldSuperContainer.addClass('error');

            if (_.isUndefined(message) === true) {
                return;
            }

            errorMessage = this.make('p', { 'class': 'help-inline' }, message);
            fieldContainer.append(errorMessage);
        },

        /************************************************************
         * EVENT CALLBACKS
         ***********************************************************/

        onCreateClick: function() {
            if (this.validateForm() !== true) {
                return false;
            }

            this.saveForm();
        }
    });
    return SignupView;
});
