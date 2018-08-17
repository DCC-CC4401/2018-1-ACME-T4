from django.db import models

from articlesApp.models import Article
from mainApp.models import Action


class Loan(Action):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)