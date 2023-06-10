from django.db import models

# Create your models here.
class tourPics(models.Model):
    heading = models.CharField(max_length=250, null=True)
    image = models.ImageField(upload_to='tourPics')
    description = models.TextField()

    def __str__(self):
        return self.heading

class teamPics(models.Model):
    memberName = models.CharField(max_length=250)
    image = models.ImageField(upload_to='teamPics')
    description = models.TextField()

    def __str__(self):
        return self.memberName
