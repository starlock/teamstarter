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
```
    user:
        email           [varchar 255]   User e-mail
        password        [varchar 255]   User Password
        bio             [varchar 120]   User biography
```

```
    project:
        name            [varchar 120]   Project name
        description     [varchar 65535] Project description
```
