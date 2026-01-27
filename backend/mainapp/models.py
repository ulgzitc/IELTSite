from django.db import models


class Test(models.Model):
    title = models.CharField()
    text = models.TextField()


    def __str__(self):
        return self.title
    