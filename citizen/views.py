import json
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import CitizenModel



def index(request):
    articles = CitizenModel.objects.all()[:30]
    context= {
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

