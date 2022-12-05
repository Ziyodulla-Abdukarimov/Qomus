from django.db import models
from accounts.models import Client


# Create your models here.
class Quiz(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=1000)
    answer1 = models.CharField(max_length=500)
    answer2 = models.CharField(max_length=500)
    answer3 = models.CharField(max_length=500)
    answer4 = models.CharField(max_length=500)
    true = models.IntegerField(max_length=2)
    question_range = models.IntegerField(max_length=3)

    def __str__(self):
        return self.question[:100]


class Score(models.Model):
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    res_rank = models.IntegerField(max_length=2, default=0)
    ans_time = models.IntegerField(max_length=2, default=0)
    date1 = models.DateTimeField(auto_now=True)

