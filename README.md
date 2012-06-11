teamstarter
===========

Our 24hbc project: Kickstarter, but teambuilding rather than fundraising

#API documentation for Teamstarter

## API Endpoints
All API endpoints reside under the root url ```/api/1```

```
End point               Method  Action
/user/create            POST    Create a new User [email, password]
/user/<user-id>         PUT     Modify User [bio]
/user/<user-id>         GET     Get model properties for given User

/project/create         POST    Create a new project [name, description]
/project/<project-id>   PUT     Modify project [name, description]
/project/<project-id>   GET     Get model properties for given Project
```

## Models
Description of model properties used to describe models in the API

### User
```
email           [varchar 255]   User e-mail
password        [varchar 255]   User Password
bio             [varchar 120]   User biography
created_at      [timestamp]     When user account was created
modified_at     [timestamp]     When user was last modified
```

### Project
```
name            [varchar 120]   Project name
description     [varchar 65535] Project description
created_at      [timestamp]     When project was created
modified_at     [timestamp]     When project was last modified
```

# Included JavaScript libraries
    jQuery 1.7.2
    Underscore.js 1.3.3
    Mustache.js 0.5.0-dev
    Backbone 0.9.2
    RequireJS 2.0.1
    RequireJS Text Plugin 2.0.0
