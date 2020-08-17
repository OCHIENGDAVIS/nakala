import json
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import CitizenModel
import runner

def clean_duplicates():
    for title in CitizenModel.objects.values_list('title', flat=True).distinct():
        CitizenModel.objects.filter(pk__in=CitizenModel.objects.filter(title=title).values_list('id', flat=True)[1:]).delete()


def index(request):
    clean_duplicates()
    articles = CitizenModel.objects.all().distinct().order_by('-order_by')
    context = {
        'articles': articles,
        'title': 'Citizen'
    }
    return render(request, 'citizen/index.html', context)


def detail(request, id):
    article = get_object_or_404(CitizenModel, id=id)
    print(article)
    context = {
        'article': article,
        'title': 'Citizen | Detail'
    }
    return render(request, 'citizen/detail.html', context)




