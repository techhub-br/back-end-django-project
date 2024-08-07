from django.shortcuts import render, get_object_or_404
from techhub.models import Projects, Articles

def about_us(request):
    return render(request, 'techhub/home.html')

def projects(request):
    projects = Projects.objects.order_by("data").filter(publish=True)
    
    return render(request, 'techhub/projects.html', {"projects":projects})

def articles(request):
    articles = Articles.objects.all()

    return render(request, 'techhub/articles.html', {"articles":articles})

def videos(request):
    return render(request, 'techhub/videos.html')

def project(request, project_id):
    project = get_object_or_404(Projects, pk=project_id)
    return render(request, 'techhub/project.html', {"project": project})

def article(request, article_id):
    article = get_object_or_404(Articles, pk=article_id)
    return render(request, 'techhub/article.html', {"article": article})
