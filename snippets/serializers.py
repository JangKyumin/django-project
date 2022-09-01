from django.contrib.auth.models import User
from rest_framework import serializers

from snippets.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
        owner = serializers.ReadOnlyField(source='owner.username')
        # fields = '__all__' : 모든 필드를 json 처리
        # exclude = ['title'] : 특정 필드 제외 처리


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']
        snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
