from django.db import models


MONTH_CHOICES = (
    ('1', "1"),
    ('2', "2"),
    ('3', "3"),
    ('4', "4"),
)

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
          return self.title
    


class Add(models.Model):
    title = models.CharField(max_length=200)
    quiz1 = models.CharField(max_length=200)
    quiz2 = models.CharField(max_length=200)
    quiz3 = models.CharField(max_length=200)
    quiz4 = models.CharField(max_length=200)
    monthh = models.CharField(max_length=9,choices=MONTH_CHOICES,default='1')
    category = models.ForeignKey(Quiz, on_delete=models.CASCADE, default=1)

    def __str__(self):
          return self.title

