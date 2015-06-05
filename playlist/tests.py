from django.test import TestCase

from playlist.models import SlackUser, Song
from playlist.service import PlaylistService, RepeatRecommendationService

reco_service = RepeatRecommendationService()

class PlaylistServiceTest(TestCase):
    def test_enqueue(self):
        p = PlaylistService(reco_service)
        u = SlackUser(username='foo')

        first_song = Song(u, 'youtube', 'https://www.youtube.com/watch?v=-fZfDjr4slI')
        second_song = Song(u, 'youtube', 'https://www.youtube.com/watch?v=Sqc9KwGgL4o')
        third_song = Song(u, 'youtube', 'https://www.youtube.com/watch?v=3UfU69ga9U8')

        p.enqueue(first_song)
        p.enqueue(second_song)
        p.enqueue(third_song)

        self.assertEqual(p.get_next(), first_song)
        self.assertEqual(p.get_next(), second_song)
        self.assertEqual(p.get_next(), third_song)

    def test_dequeue(self):
        p = PlaylistService(reco_service)
        u = SlackUser(username='foo')

        first_song = Song(u, 'youtube', 'https://www.youtube.com/watch?v=-fZfDjr4slI')
        second_song = Song(u, 'youtube', 'https://www.youtube.com/watch?v=Sqc9KwGgL4o')
        third_song = Song(u, 'youtube', 'https://www.youtube.com/watch?v=3UfU69ga9U8')

        p.enqueue(first_song)
        p.enqueue(second_song)
        p.enqueue(third_song)

        self.assertEqual(p.get_next(), first_song)
        p.dequeue(second_song)
        self.assertEqual(p.get_next(), third_song)

    def test_recommendations(self):
        reco_service_l = RepeatRecommendationService()
        p = PlaylistService(reco_service_l)
        u = SlackUser(username='foo')

        first_song = Song(u, 'youtube', '1')
        second_song = Song(u, 'youtube', '2')
        third_song = Song(u, 'youtube', '3')

        p.enqueue(first_song)
        p.enqueue(second_song)
        p.enqueue(third_song)

        self.assertEqual(p.get_next(), first_song)
        self.assertEqual(p.get_next(), second_song)
        self.assertEqual(p.get_next(), third_song)

        self.assertEqual(p.get_next(), first_song)
        self.assertEqual(p.get_next(), second_song)
        self.assertEqual(p.get_next(), third_song)

        self.assertEqual(p.get_next(), first_song)
        self.assertEqual(p.get_next(), second_song)
        self.assertEqual(p.get_next(), third_song)

        self.assertEqual(p.get_next(), first_song)
        self.assertEqual(p.get_next(), second_song)
        self.assertEqual(p.get_next(), third_song)
