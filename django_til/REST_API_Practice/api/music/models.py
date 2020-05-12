from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=30)
    def musics_count(self):
        return self.music_set.count()

class Music(models.Model):
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=50)
    def music_artist(self):
        return self.artist.name

class Comment(models.Model):
    music = models.ForeignKey(
        Music,
        on_delete=models.CASCADE
    )
    content = models.TextField()