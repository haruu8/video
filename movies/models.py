from django.db import models

class MovieContent(models.Model):

    class Meta(object):
        db_table = 'movie'

    title = models.CharField(verbose_name='タイトル', max_length=255, null=False)
    discription = models.CharField(verbose_name='説明欄', max_length=500, null=True)
    movie = models.FileField(
        upload_to='media/%Y/%m/%d/',
        verbose_name='添付ファイル',
        # validators=[FileExtensionValidator(['pdf', ])],
    )
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    class Meta(object):
        db_table = 'comment'

    text = models.CharField(verbose_name='コメント', max_length=255, null=False)
    approved_comment = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text