from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', Index, name='index-page'),
    re_path(r'pagination/prev-next/(?P<pg>\d*/?)', Pagination_pvnx, name='pg_pvnx'),
    # details paper
    re_path(r'details/(?P<paper_id>\d+)/', Details, name='details-page'),

]

