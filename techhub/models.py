from django.db import models
from datetime import datetime

class Projects(models.Model):

    CATEGORY_DATA = [
        {"DESENVOLVIMENTO WEB", "desenvolvimento web"},
        {"ANÁLISE DE DADOS", "analise de dados"},
        {"SEGURANÇA DA INFORMAÇÃO", "segurança da informação"},
        {"INTELIGÊNCIA ARTIFICIAL", "inteligência artificial"}
    ]

    title = models.CharField(max_length=100, null=False, blank=False)
    legend = models.CharField(max_length=500, null=False, blank=False)
    image = models.ImageField(upload_to="fotos/%Y/%m/%d", blank=True)
    description = models.TextField(max_length=25000, null=False, blank=False)
    category = models.CharField(max_length=100, choices=CATEGORY_DATA, default='')
    publish = models.BooleanField(default=False)
    data = models.DateTimeField(default=datetime.now, blank=False)
    
    def __str__(self):
        return f'project[title={self.title}]'
    
class Articles(models.Model):

    CATEGORY_DATA = [
        {"DESENVOLVIMENTO WEB", "desenvolvimento web"},
        {"ANÁLISE DE DADOS", "analise de dados"},
        {"SEGURANÇA DA INFORMAÇÃO", "segurança da informação"},
        {"INTELIGÊNCIA ARTIFICIAL", "inteligência artificial"}
    ]

    title = models.CharField(max_length=100, null=False, blank=False)
    legend = models.CharField(max_length=500, null=False, blank=False)
    image = models.ImageField(upload_to="fotos/%Y/%m/%d", blank=True)
    description = models.TextField(max_length=25000, null=False, blank=False)
    category = models.CharField(max_length=100, choices=CATEGORY_DATA, default='')
    publish = models.BooleanField(default=False)
    data = models.DateTimeField(default=datetime.now, blank=False)
    
    def __str__(self):
        return f'articles[title={self.title}]'
    