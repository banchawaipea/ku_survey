from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from .models import Paper
from django.core.paginator import Paginator

def Index(request):
    
    data_papers = Paper.objects.all().order_by('-id') # ดึงข้อมูลจาก model มาแสดง

    paginator = Paginator(data_papers, 10) # แบ่งหน้าข้อมูล
    page = paginator.get_page(1) # ดึงหน้าที่เลือกมาแสดง
    
    # context['data_paper'] = Paper.objects.all()
    # Add in a QuerySet of all the books
    # context['paper_list'] = Paper.objects.all()
    context = {
        'data_papers':data_papers,
    }
    return render(request, 'main.html', context)