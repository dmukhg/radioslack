from playlist.models import SlackUser, Song
from Queue import Queue

class PlaylistService:
    def __init__(self, reco_service):
        self.queue = []
        self.reco_service = reco_service

    def enqueue(self, song):
        self.reco_service.next_reco_for(song)
        self.queue.append(song)

    def dequeue(self, song):
        self.queue.remove(song)

    def get_next(self):
        if len(self.queue) is 0:
            el = self.reco_service.get_reco()
        else:
            el = self.queue[0]
            self.queue.remove(el)
        return el

    def enqueue_recommendation(self, song):
        self.rec_queue.append(song)

class RepeatRecommendationService:
    def __init__(self):
        self.songs = []
        self.offset = 0

    def next_reco_for(self, song):
        self.songs.append(song)

    def get_reco(self):
        el = self.songs[self.offset]
        if self.offset == len(self.songs) - 1:
            self.offset = 0
        else:
            self.offset += 1

        return el

reco_service = RepeatRecommendationService()
playlist_service = PlaylistService(reco_service)
