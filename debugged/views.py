from rest_framework import generics
from .models import Post
from .serializers import PostSerializer


class PostListView(generics.ListAPIView):
    """
    GET: List all posts
    """
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveAPIView):
    """
    GET: Retrieve a post by ID
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
