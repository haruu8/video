from django.db import models

class MovieContent(models.Model):

    class Meta(object):
        db_table = 'movie'

    title = models.CharField(max_length=255, null=False)
    discription = models.CharField(max_length=355, null=True)
    movie = models.FileField()
