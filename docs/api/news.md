# News
Supports Create, viewing, and updating articles.

## Create news articles

**Request**:

`POST` `/news/`

Parameters:

Name       | Type   | Required | Description
-----------|--------|----------|------------
title      | string | Yes      | The articles's title
body       | string | Yes      | The article's content.
status     | string | No       | The article's status. Defaults to "DRAFT". Accepts either "DRAFT" or "PUBLISHED"

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
201 Created

{
    "title":"Incantation",
    "body":"Hello, World!",
    "status":"draft",
    "author_name":"",
    "created":"2018-09-25T14:17:53+0000",
    "modified":"2018-09-25T14:17:53+0000","author":"http://0.0.0.0:8080/api/v1/users/7ed14eb1-7dd4-42b9-8b7e-7807d8eddec4/","url":"http://0.0.0.0:8080/api/v1/news/a4b3e279-7659-415f-bed5-c7de53ba902e/","id":"a4b3e279-7659-415f-bed5-c7de53ba902e"
}
```
## Get the article details

**Request**:

`GET` `/news/:id/`

Parameters:

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
    "title":"Incantation",
    "body":"Hello, World!",
    "status":"draft",
    "author_name":"",
    "created":"2018-09-25T14:17:53+0000",
    "modified":"2018-09-25T14:17:53+0000","author":"http://0.0.0.0:8080/api/v1/users/7ed14eb1-7dd4-42b9-8b7e-7807d8eddec4/","url":"http://0.0.0.0:8080/api/v1/news/a4b3e279-7659-415f-bed5-c7de53ba902e/","id":"a4b3e279-7659-415f-bed5-c7de53ba902e"
}
```


## Update article

**Request**:

`PUT/PATCH` `/news/:id/`

Parameters:

Name       | Type   | Required | Description
-----------|--------|----------|------------
title      | string | Yes      | The articles's title
body       | string | Yes      | The article's content.
status     | string | No       | The article's status. Defaults to "DRAFT". Accepts either "DRAFT" or "PUBLISHED"



*Note:*

- All parameters are optional
- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
    "title":"Incantation",
    "body":"Hello, World!",
    "status":"draft",
    "author_name":"",
    "created":"2018-09-25T14:17:53+0000",
    "modified":"2018-09-25T14:17:53+0000","author":"http://0.0.0.0:8080/api/v1/users/7ed14eb1-7dd4-42b9-8b7e-7807d8eddec4/","url":"http://0.0.0.0:8080/api/v1/news/a4b3e279-7659-415f-bed5-c7de53ba902e/","id":"a4b3e279-7659-415f-bed5-c7de53ba902e"
}
```
