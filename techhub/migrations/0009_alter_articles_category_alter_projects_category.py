# Generated by Django 5.0.7 on 2024-07-30 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techhub', '0008_alter_articles_category_alter_projects_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='category',
            field=models.CharField(choices=[('desenvolvimento web', 'DESENVOLVIMENTO WEB'), ('ANÁLISE DE DADOS', 'analise de dados'), ('SEGURANÇA DA INFORMAÇÃO', 'segurança da informação'), ('INTELIGÊNCIA ARTIFICIAL', 'inteligência artificial')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='projects',
            name='category',
            field=models.CharField(choices=[('desenvolvimento web', 'DESENVOLVIMENTO WEB'), ('ANÁLISE DE DADOS', 'analise de dados'), ('SEGURANÇA DA INFORMAÇÃO', 'segurança da informação'), ('INTELIGÊNCIA ARTIFICIAL', 'inteligência artificial')], default='', max_length=100),
        ),
    ]
