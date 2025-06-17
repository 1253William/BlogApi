from django.shortcuts import get_object_or_404

from .models import BlogPost
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import BlogPostSerializer


#Logic to fetch all posts
@api_view(['GET']) #http method to use only GET
def fetch_all_posts(request):
    posts = BlogPost.objects.all() #variable set to access all blog post records from DB
    serializer = BlogPostSerializer(posts, many=True)  #serialize all posts lists
    return Response(serializer.data) #returns the serialized data as JSON

#Fetch a post by id
@api_view(['GET'])
def fetch_post_by_id(request, id):
    post = get_object_or_404(BlogPost, id=id) #Get the post or return 404
    serializer = BlogPostSerializer(post) #serialize a single post
    return Response(
        {"message": "success",
         "data": serializer.data
    },
        status=status.HTTP_200_OK
    )


#Create a post
@api_view(['POST'])
def create_post(request):
    serializer = BlogPostSerializer(data=request.data) #deserialize incoming data

    if serializer.is_valid():
        serializer.save()  # Save valid data to DB
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#Update a post by id
@api_view(['PUT'])
def update_post(request, id): #id is the primary key the unique key
    post = get_object_or_404(BlogPost, id=id)
    serializer = BlogPostSerializer(post, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#Delete a post by id
@api_view(['DELETE'])
def delete_post(request, id):
    post = get_object_or_404(BlogPost, id=id)
    post.delete()
    return Response({"message": "post deleted successfully"},
                    status=status.HTTP_204_NO_CONTENT
                    )



