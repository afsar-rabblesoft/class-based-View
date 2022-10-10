from dataclasses import field
from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = [
        #     "id",
        #     "title",
        #     "author",
        #     "email",
        # ]  # Describe all fields you want to fetch
        fields = "__all__"
