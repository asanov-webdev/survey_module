from django.contrib.postgres.fields import ArrayField
from django.db import models


QUESTION_ANSWER_TYPE_CHOICES = [
    ('CH', 'CHOICE'),
    ('MU', 'CHOICE_MULT'),
    ('VA', 'VALUE'),
    ('TE', 'TEXT'),
]


class Test(models.Model):
    title = models.CharField(max_length=120)
    question_order = ArrayField(models.IntegerField(), blank=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    text = models.TextField()
    answer_type = models.CharField(
        max_length=2,
        choices=QUESTION_ANSWER_TYPE_CHOICES,
        default='CH'
    )
    answer_variants = ArrayField(models.TextField(), blank=True)
    correct_answer_variants = ArrayField(
        models.SmallIntegerField(), blank=True)

    def __str__(self):
        return self.text
