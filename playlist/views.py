from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from playlist.models import Song, SlackUser
from playlist.serializers import SongSerializer

@api_view(['GET'])
def song_next(request, offset=0):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        user = SlackUser.objects.get(username='dipanjan')
        song = Song(user=user, source='youtube', link='https://www.youtube.com/watch?v=kde0XOnxeJM')
        serializer = SongSerializer(song)
        return Response(serializer.data)
