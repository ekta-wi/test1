from django.db import models
from django.utils import timezone


# Create your models here.

#models.Model implies it is DJango model and thus is to be saved into the DB
#Model name should start with uppercase
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    #CharField - text field with a limit on length
    title = models.CharField(max_length=200)
    #TextField - text field without a limit on length
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    # def means defining a method (name can have lowercase and underscores)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
