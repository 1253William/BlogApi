//Model - Database Schema (Skeleton for the database)

//View - Business Logic using @app_view

//HTTP METHODS - GET() - retrieve/fetch, POST()- create, PUT() - update/edit, DELETE()- remove

//App Features:
- An API to:
- Create a post ()
- Read/Retrieve all posts
- Read a single post
- Update a post
- Delete a post


//Installation
django-admin startproject blogposts
cd blogposts
python manage.py startapp blogapp

-Add your app to settings
-Make your database schema in models.py
-Run the migrations on the schema

python manage.py makemigrations
python manage.py migrate

-Set urls
-Bind app url to project url

- Create a view functions
- Add rest framework to settings

-run python manage.py createsuperuser
Will | Will12345 | williamofosuparwar@gmail.com

-Add a serializer
-Test


