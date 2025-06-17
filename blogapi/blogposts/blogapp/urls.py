from django.urls import path
from . import views

urlpatterns = [
    path('api/posts', views.fetch_all_posts, name='fetch_all_posts'), #Get all posts route
    path('api/create', views.create_post, name='create_post'), #Create a new post
    path('api/posts/<int:id>', views.fetch_post_by_id, name='fetch_post_by_id'), #Get a post by id route
    path('api/update/<int:id>', views.update_post, name='update_post'), #Update a post by id route
    path('api/delete/<int:id>', views.delete_post, name='delete_post'),     #Delete a post by id route
]