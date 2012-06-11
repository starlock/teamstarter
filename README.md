teamstarter
===========

Our 24hbc project: Kickstarter, but teambuilding rather than fundraising

#API documentation for Teamstarter


All API endpoints reside under the root url ```/api/1```

```
End point               Method              Action
/user/create            POST                Create a new user
    email:              E-mail to create user with [varchar 255]
    password:           Password used to authenicate user, [varchar 255]

/user/<user-id>         GET                 Get information regarding user
/user/<user-id>         PUT                 Modify user
    bio:        User biography, [varchar 120]

/project/create         POST                Create a new project
    name:               Project name [varchar 120]
    description:        Project description, [varchar 65535]

/project/<project-id>   PUT                 Modify project
/project/<project-id>   GET                 Get information regarding project


Models:
    user:
        email           [varchar 255]   cannot be modified after creation
        password        [varchar 255]
        bio             [varchar 120]

    project:
        name            [varchar 120]
        description     [varchar 65535]
```
