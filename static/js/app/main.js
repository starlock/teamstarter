define([
    'text!template/layout/main.html',
    'app/layout/navigation',

    'app/view/discover',

    'app/view/project/create',
    'app/view/project/show',

    'app/util'
], function(
    BaseMarkup,
    NavigationLayout,

    DiscoverView,

    CreateProjectView,
    ShowProjectView,

    Utility
) {
    // Application context
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
            var self = this;
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
                        window.session = e;
                        self.renderNavigation();
                    },
                    error: function() {
                        console.log('Failed to login');
                    },
                });
            }
        },

        populateSession: function() {
            var user_id = window.clientSession.id;
            var User = Backbone.Model.extend({urlRoot : '/api/user/' + user_id});
            var user = new User(window.clientSession);
            window.session = user;
        },

        renderNavigation: function() {
            var navigation = new NavigationLayout();
            if (_.isUndefined(this.currentNavigation) !== true) {
                this.currentNavigation.remove();
            }

            this.currentNavigation = navigation;
            this.$('#nav-container').append(navigation.render().$el);
            return this;
        }
    });

    var Workspace = Backbone.Router.extend({
        routes: {
            '': 'indexHandler',

            'discover': 'discoverHandler',

            'project/create': 'createProjectHandler',
            'project/:id': 'showProjectHandler'
        },

        indexHandler: function() {
            this.discoverHandler();
        },

        /********************************************************************
         * DISCOVER VIEW
         *******************************************************************/

        discoverHandler: function() {
            changeContentView(new DiscoverView());
        },

        /********************************************************************
         * PROJECT RELATED VIEWS
         *******************************************************************/

        createProjectHandler: function() {
            changeContentView(new CreateProjectView());
        },

        showProjectHandler: function(pid) {
            changeContentView(new ShowProjectView());
        }
    });

    var getContentViewContainer = function() {
        var node = app.viewContainerNode;
        if (_.isUndefined(node) !== true) {
            return node;
        }

        node = $('#pageholder');
        app.viewContainerNode = node;
        return node;
    };

    var changeContentView = function(view) {
        var currentView = app.currentView;
        if (_.isUndefined(currentView) !== true) {
            console.log('Time to remove content view');
            currentView.$el.fadeOut(function() {
                currentView.remove();
                app.currentView = undefined;
                _setContentView(view);
            });
            return;
        }
        _setContentView(view);
    };

    var _setContentView = function(view) {
        console.log('Time to add content view', view);
        view.render();

        var container = getContentViewContainer();
        console.log('Content view container', container);
        app.currentView = view;

        var viewElement = view.$el;
        viewElement.hide();
        container.append(viewElement);
        viewElement.fadeIn();
    };

    var onTriggeredRoute = function(path) {
        // Proceed if path is given, otherwise stay put
        if (_.isUndefined(path) === true || path.length === 0) {
            return;
        }

        app.router.navigate(path, {
            trigger: true
        });
    };

    var initRouter = function() {
        var instance = app.router = new Workspace();

        Utility.Mediator.on('page:navigate', onTriggeredRoute);
        Backbone.history.start({
            pushState: true
        });
    };

    var onDocumentReady = function() {
        var bodyNode = $('body');
        var container = $('<div/>');
        var curtainNode = $('#curtain');

        // Render application view
        var view = app.view = new ApplicationView();
        view.populateSession();
        container.append(view.render().$el);

        // Prepare application view for coming effects
        container.hide();
        bodyNode.append(container);

        // Swap curtain against prepared application DOM
        curtainNode.fadeOut(function() {
            curtainNode.remove();
        });
        container.fadeIn();
        initRouter();
    };

    // Listen to the DOMReady event
    $(onDocumentReady);
});
