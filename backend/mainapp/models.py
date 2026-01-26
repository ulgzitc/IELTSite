from django.db import models



class Listening(models.Model):
    title = models.CharField(max_length=300, null=False, blank=False)
    audio = models.FileField(null=False, blank=Flase)
    part1 = models.ForeignKey()
    part2 = models.ForeignKey()
    part3 = models.ForeignKey()
    part4 = models.ForeignKey()
#    user = models.ForeignKey()