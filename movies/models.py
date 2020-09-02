from django.db import models

class MovieContent(models.Model):

    class Meta(object):
        db_table = 'movie'

    title = models.CharField(verbose_name='タイトル', max_length=255, null=False)
    discription = models.CharField(verbose_name='説明欄', max_length=500, null=True)
    movie = models.FileField(
        upload_to='uploads/%Y/%m/%d/',
        verbose_name='添付ファイル',
        # validators=[FileExtensionValidator(['pdf', ])],
    )
    created_at = models.DateTimeField(auto_now_add=True)
