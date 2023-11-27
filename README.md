# FastAPI Blog API

This is a basic CRUD API for a blog using FastAPI.

## Endpoints

### Get All Blogs

`GET /blog`- Fetches all blogs from the database with optional query parameters:

-   `limit`  - limits number of blogs returned
-   `published`  - filters published/unpublished blogs
-   `sort`  - sorts by field

### Get Single Blog

`GET /blog/{id}` - Fetches a single blog by its ID passed in as a path parameter

### Get Blog Comments

`GET /blog/{id}/comments` - Gets comments for a single blog by its ID

### Create Blog

`POST /blog` - Creates a new blog from data passed in the request body:

Copy code

`{
  "title": "Post title",
  "body": "Post body",
  "published": true/false
}`

Uses Pydantic models for data validation.

## Built With

-   FastAPI
-   Pydantic
-   Python 3

Overall, this provides a starting point for a FastAPI powered blog or article API with major CRUD functionality.
