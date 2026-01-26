from django.db import models




class Test(models.Model):
    title = models.CharField(null=False, blank=False)
    
    def __str__(self):
        return self.title
    




class Questions(models.Model):
    CHOICE_TYPES = (
        ('gap_fill', 'Gap FIll (Inline)'),
        ('grid', 'Grid'),
        ('multiple_choice', 'Multiple Choices')
    )


    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question_type = models.CharField(max_length=20, choices=CHOICE_TYPES)

    content = models.TextField()

    data = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.get_question_type_display()} - {self.test.title}"    