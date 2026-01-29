from django.db import models


class Test(models.Model):
    CHOICE_TYPES = {
        'radios' : "Radios",
        'inline' : "Inline",
        'inline_tab' : "Inline Tab",
        'checkbox' : "Checkbox",
    }

    title = models.CharField()
    text = models.TextField()
    qtype = models.CharField(choices=CHOICE_TYPES)


    def __str__(self):
        return self.title

    