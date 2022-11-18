from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from .models import Paper

def Index(request):
    data_papers = Paper.objects.all()
    context = {
        'data_papers':data_papers
    }
    # context['data_paper'] = Paper.objects.all()
    # Add in a QuerySet of all the books
    # context['paper_list'] = Paper.objects.all()
    return render(request, 'main.html', context)