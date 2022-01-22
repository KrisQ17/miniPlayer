from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    login = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    mail = models.CharField(max_length=255)

    def toJson(self):
        return {'id': self.id, 'name': self.name}


class Video(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    miniature = models.TextField(max_length=4000)
    path = models.TextField(max_length=4000)

    def calculateRating(self):
        stats = VideoStat.objects.filter(video=self.id)
        rating = 0
        count = 0
        for stat in stats:
            count += 1
            rating += stat.rating
        if count == 0:
            return 0
        else:
            result = rating/count
            return result

    def ratingCount(self):
        stats = VideoStat.objects.filter(video=self.id)
        return stats.count()

    def toJson(self):
        return {'id': self.id, 'name': self.name, 'category': self.category, 'miniature': self.miniature, 'path': self.path,
         'rating': self.calculateRating(), 'rating_count': self.ratingCount()}

class VideoStat(models.Model):
    id = models.BigAutoField(primary_key=True)
    video = ForeignKey(Video, on_delete=models.CASCADE)
    user = ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(max_length=2)

    def toJsonRating(self):
        return {'id': self.id, 'rating': self.rating}

class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    video = ForeignKey(Video, on_delete=models.CASCADE)
    user = ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    text = models.TextField(max_length=1000)

    def toJson(self):
        return {'id': self.id, 'user': self.user.toJson(), 'date': self.date, 'text': self.text}