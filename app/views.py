from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from .models import Paper
from django.core.paginator import Paginator

def Index(request):
    
    rows = Paper.objects.all().order_by('-id') # ดึงข้อมูลจาก model มาแสดง
    pgn = Paginator(rows, 8) # แบ่งหน้าข้อมูล
    page = pgn.get_page(1) # ดึงหน้าที่เลือกมาแสดง
    context = {
        'page':page,
    }
    
    # context['data_paper'] = Paper.objects.all()
    # Add in a QuerySet of all the books
    # context['paper_list'] = Paper.objects.all()
    return render(request, 'index.html', context)

def Details(request, paper_id):
    context = {
        'paper':Paper.objects.get(id=paper_id)
    }
    return render(request, 'details.html', context)

def Pagination_pvnx(request, pg):
    if pg == None:
        pg = 1
    
    rows = Paper.objects.all().order_by('-id') # ดึงข้อมูลจาก model มาแสดง
    pgn = Paginator(rows, 2) # แบ่งหน้าข้อมูล
    page = pgn.get_page(pg) # ดึงหน้าที่เลือกมาแสดง
    context = {
        'page':page,
    }
    return render(request, 'pagination_pvnx.html', context)