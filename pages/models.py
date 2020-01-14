from django.db import models


class Note(models.Model):
    title = models.CharField('Note title', max_length=300)
    note_thumbnail = models.ImageField('Note thumbnail', 
        upload_to='note_thumbnails',
        default='thumbnail.png')
    note = models.TextField('Note description (Markdown)')
    written_at = models.DateTimeField(auto_now=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
