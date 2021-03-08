from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    choice_text = models.CharField(max_length=200, default = " ")
    choice_text2 = models.CharField(max_length=200, default = " ")
    def __str__(self):
        return self.question_text

    # class Choice(models.Model):
    #     # question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #     choice_text = models.CharField(max_length=200)
    #     choice_text2 = models.CharField(max_length=200, default = " ")
    #     votes = models.IntegerField(default=0)
    #     def __str__(self):
    #         return self.choice_text
    #         return self.choice_text2