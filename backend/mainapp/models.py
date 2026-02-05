from django.db import models


class Test(models.Model):
    CHOICE_TYPES = {
        'radios' : "Radios",
        'inline' : "Inline",
        'inline_tab' : "Inline Tab",
        'checkbox' : "Checkbox",
        'tabular' : "Tabular (JSON)",
        'grid' : "Grid (JSON)",
        'assign' : "Assign (JSON)",
    }

    title = models.CharField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    jsondata = models.JSONField(default=dict, null=True, blank=True)
    qtype = models.CharField(choices=CHOICE_TYPES)


    def __str__(self):
        return self.title

