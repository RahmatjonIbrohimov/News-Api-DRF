from django.db import models

# Create your models here.
class NewsKeeperModel(models.Model):
    photo = models.URLField()
    title = models.CharField(max_length=255)
    url = models.URLField()
    description = models.TextField()
    date = models.CharField(max_length=11)

    class Meta:
        db_table = 'LatestNewsApiV2'
