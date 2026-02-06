from django.db import models


class Test(models.Model):
    CHOICE_TYPES = {
        'radios' : "Radios",
        'inline' : "Inline",
        'inline_list' : "Inline List",
        'inline_tab' : "Inline Tab",
        'checkbox' : "Checkbox",
        'tabular' : "Tabular",
        'grid' : "Grid",
        'assign' : "Assign",
        'draganddrop' : "Drag-and-Drop",
    }

    title = models.CharField(null=True, blank=True)
    data = models.JSONField(default=dict, null=True, blank=True)
    qtype = models.CharField(choices=CHOICE_TYPES)


    def __str__(self):
        return self.title

