teamstarter
===========

Our 24hbc project: Kickstarter, but teambuilding rather than fundraising

#API documentation for Teamstarter

## API Endpoints
All API endpoints reside under the root url ```/api/1```
```
End point               Method  Action
/user/create            POST    Create a new user [email, password]
/user/<user-id>         GET     Get information regarding user
/user/<user-id>         PUT     Modify user [bio]

/project/create         POST                Create a new project
    name:               Project name [varchar 120]
    description:        Project description, [varchar 65535]

/project/<project-id>   PUT                 Modify project
/project/<project-id>   GET                 Get information regarding project
```

## Models
### User
```
email           [varchar 255]   User e-mail
password        [varchar 255]   User Password
bio             [varchar 120]   User biography
```

### Project
```
name            [varchar 120]   Project name
description     [varchar 65535] Project description
```

## Included JavaScript libraries
    jQuery 1.7.2
    Underscore.js 1.3.3
    Mustache.js 0.5.0-dev
    Backbone 0.9.2
    RequireJS 2.0.1
    RequireJS Text Plugin 2.0.0
