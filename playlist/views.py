from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from playlist.models import Song, SlackUser
from playlist.serializers import SongSerializer
from playlist.service import playlist_service

@api_view(['GET'])
def song_next(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        song = playlist_service.get_next()
        serializer = SongSerializer(song)
        return Response(serializer.data)
