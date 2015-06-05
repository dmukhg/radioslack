from django.forms import widgets
from rest_framework import serializers
from playlist.models import Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('user', 'source', 'link')
