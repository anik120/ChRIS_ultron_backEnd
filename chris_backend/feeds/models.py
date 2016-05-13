from django.db import models

# Create your models here.

class Note(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    class Meta:
        ordering = ('creation_date',)

    def __str__(self):
        return self.title


class Feed(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    owner = models.ForeignKey('auth.User', related_name='feed')
    note = models.ForeignKey(Note, related_name='feed')
    
    class Meta:
        ordering = ('creation_date',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        Save a new note before saving the feed
        """
        note = Note()
        note.save()
        self.note = note
        super(Feed, self).save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=20)
    feeds = models.ManyToManyField(Feed, related_name='tag')

    def __str__(self):
        return self.name


class Comment(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='comment')
    feed = models.ForeignKey(Feed, related_name='comment')

    class Meta:
        ordering = ('creation_date',)

    def __str__(self):
        return self.title
