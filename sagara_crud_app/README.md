## Requirements
- Docker Desktop
- MySQL


## 1. Running app
- Setting your local db credentials in .env file
- Run command 'cd sagara_crud_app'
- Run command 'docker-compose build --no-cache'
- Run command 'docker-compose up'

## Endpoints User

1. http:127.0.0.1:5000/register  [POST]
   using form-data body in postman:

   "name": "NN"
   "password":"klm"
   "username":"user1"
   "email":"ert@ini.com"

2. http:127.0.0.1:5000/login  [POST]
   using form-data body in postman:

   "username":"user1"
   "password":"klm"

3. http:127.0.0.1:5000/profile  [GET] **
   get all user
   
4. http:127.0.0.1:5000/profile/<int:user_id>  [GET]**
   get user by id

5. http:127.0.0.1:5000/update_profile/<int:user_id>  [PUT] **
   update all or several field
   using form-data body in postman:

   "name": "NN new"
   "password":"klmNew"
   "username":"user1New"
   "email":"ert@ini.com"

6. http:127.0.0.1:5000/logout  [GET]**
   destroy session and logout



## Endpont Posting Blog

1. http:127.0.0.1:5000/add  [POST]
   using form-data body in postman:

   "title": "Title Post"
   "post":"Content Post"


2. http:127.0.0.1:5000/posts  [GET] **
   get all posts
   
3. http:127.0.0.1:5000/post/<int:post_id>  [GET]**
   get post by id

4. http:127.0.0.1:5000/update/<int:post_id>  [PUT] **
   update all or several field
   using form-data body in postman:

  "title": "Title Post Update"
   "post":"Content Post Update"

5. http:127.0.0.1:5000/delete/<int:post_id>  [DELETE]**
   delete post by id


** : these endpoints need login first to be accessed