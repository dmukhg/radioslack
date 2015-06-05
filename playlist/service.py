from playlist.models import SlackUser, Song
import simplejson as json
import pickle
from Queue import Queue

class PlaylistService:
    def __init__(self, reco_service):
        self.reco_service = reco_service
        self.load()

    def enqueue(self, song):
        self.load()
        self.reco_service.next_reco_for(song)
        self.queue.append(song)
        self.dump()

    def dequeue(self, song):
        self.load()
        self.queue.remove(song)
        self.dump()

    def get_next(self):
        self.load()
        if len(self.queue) is 0:
            el = self.reco_service.get_reco()
        else:
            el = self.queue[0]
            self.queue.remove(el)
        self.dump()
        return el

    def dump(self):
        print 'saving to lemon'
        fh = open('lemon.pickle', 'wb')
        pickle.dump(self.queue, fh)

    def load(self):
        print 'loading from lemon'
        fh = open('lemon.pickle', 'r')
        try:
            self.queue = pickle.load(fh)
        except:
            self.queue = []
            self.dump()


class RepeatRecommendationService:
    def __init__(self):
        self.load()
    
    def next_reco_for(self, song):
        self.load()
        self.songs.append(song)
        self.dump()

    def get_reco(self):
        self.load()
        el = self.songs[self.offset]
        if self.offset == len(self.songs) - 1:
            self.offset = 0
        else:
            self.offset += 1

        self.dump()
        return el

    def dump(self):
        print 'saving to mango and chili'
        fh = open('mango.pickle', 'wb')
        fh1 = open('chilli.pickle', 'wb')
        pickle.dump(self.songs, fh)
        pickle.dump(self.offset, fh1)

    def load(self):
        print 'loading from mango and chilli'
        fh = open('mango.pickle', 'r')
        fh1 = open('chilli.pickle', 'r')
        try:
            self.songs = pickle.load(fh)
            self.offset = pickle.load(fh1)
        except:
            self.songs = []
            self.offset = 0
            self.dump()




reco_service = RepeatRecommendationService()
playlist_service = PlaylistService(reco_service)
