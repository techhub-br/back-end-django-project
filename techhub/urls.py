from django.urls import path
from techhub.views import about_us, projects, articles, videos, project, article

urlpatterns = [
    path('', about_us, name='about_us'),
    path('about_us/', about_us, name='about_us'),
    path('projects/', projects, name='projects'),
    path('articles/', articles, name='articles'),
    path('videos/', videos, name='videos'),
    path('project/<int:project_id>', project, name='project'),
    path('article/<int:article_id>', article, name='article'),
]
