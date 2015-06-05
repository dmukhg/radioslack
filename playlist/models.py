from django.db import models

class SlackUser(models.Model):
    username = models.CharField(max_length=100, blank=False, unique=True)

class Song(models.Model):
    SOURCE_CHOICES = (
            ('youtube', 'youtube'),
            ('soundcloud', 'SoundCloud')
    )

    user = models.ForeignKey('SlackUser')
    source = models.CharField(max_length=10, choices=SOURCE_CHOICES)
    link = models.CharField(max_length=1000, blank=False)
    order = models.IntegerField(default=1)

    def __repr__(self):
        return ' <Song: ' + str(self.source) + ' >'

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False
