# Users
Supports registering, viewing, and updating user accounts.

## Register a new user account

**Request**:

`POST` `/users/`

Parameters:

Name       | Type   | Required | Description
-----------|--------|----------|------------
username   | string | Yes      | The username for the new user.
password   | string | Yes      | The password for the new user account.
first_name | string | No       | The user's given name.
last_name  | string | No       | The user's family name.
email      | string | No       | The user's email address.
bio        | string | No       | The user's bio

*Note:*

- Not Authorization Protected

**Response**:

```json
Content-Type application/json
201 Created

{
  "id": "6d5f9bae-a31b-4b7b-82c4-3853eda2b011",
  "url": "http://0.0.0.0:8080/api/v1/users/6d5f9bae-a31b-4b7b-82c4-3853eda2b011/",
  "username": "johndoo",
  "first_name": "John",
  "last_name": "Doe",
  "bio": "dummy dev",
  "email": "johndoe@example.com",
  "auth_token": "132cf952e0165a274bf99e115ab483671b3d9ff6"
}
```

The `auth_token` returned with this response should be stored by the client for
authenticating future requests to the API. See [Authentication](authentication.md).


## Get a user's profile information

**Request**:

`GET` `/users/:id`

Parameters:

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "id": "6d5f9bae-a31b-4b7b-82c4-3853eda2b011",
  "url": "http://0.0.0.0:8080/api/v1/users/6d5f9bae-a31b-4b7b-82c4-3853eda2b011/",
  "username": "johndoe",
  "first_name": "John",
  "last_name": "Doe",
  "profile":
    {
      "bio":"dummy dev",
      "user":"http://0.0.0.0:8080/api/v1/users/6d5f9bae-a31b-4b7b-82c4-3853eda2b011/",
      "url":"http://0.0.0.0:8080/api/v1/profile/2edcfbb1-3bd6-450e-b640-7d301dbeb1ed/"
    },
  "email": "johndoe@example.com",
}
```


## Update your profile information

**Request**:

`PUT/PATCH` `/users/:id`

Parameters:

Name       | Type   | Description
-----------|--------|---
first_name | string | The first_name of the user object.
last_name  | string | The last_name of the user object.
email      | string | The user's email address.
bio        | string | No       | The user's bio



*Note:*

- All parameters are optional
- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "id": "6d5f9bae-a31b-4b7b-82c4-3853eda2b011",
  "url": "http://0.0.0.0:8080/api/v1/users/6d5f9bae-a31b-4b7b-82c4-3853eda2b011/",
  "username": "johndoe",
  "first_name": "John",
  "last_name": "Doe",
  "profile":
    {
      "bio":"dummy dev",
      "user":"http://0.0.0.0:8080/api/v1/users/6d5f9bae-a31b-4b7b-82c4-3853eda2b011/",
      "url":"http://0.0.0.0:8080/api/v1/profile/2edcfbb1-3bd6-450e-b640-7d301dbeb1ed/"
    },
  "email": "johndoe@example.com",
}
```
