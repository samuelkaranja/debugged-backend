from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'subtitle', 'content', 'author', 'image_url', 'created_at', 'updated_at']

    def get_image_url(self, obj):
        return obj.image.url if obj.image else None
