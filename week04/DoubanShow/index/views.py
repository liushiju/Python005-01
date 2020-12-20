from django.shortcuts import render
from django.http import HttpResponse
from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine,Table,Column,Integer,String,MetaData,ForeignKey,desc,func,and_,or_,not_
from sqlalchemy.ext.declarative import declarative_base
from .models import CommentStar
from django.forms.models import model_to_dict

def index(request):    
    comments=CommentStar.objects.filter(star__gt='allstar30 rating')
    for comment in comments:
        comment.star=comment.star[7:8]+'星'
    return render(request, 'index.html',locals())


def search(request):
    search_str = request.GET.get('q')
    if search_str not in ['3星', '4星', '5星']:
        return render(request, '404.html')
    if search_str == '3星':
        comments=CommentStar.objects.filter(star='allstar30 rating')
        for comment in comments:
            comment.star=comment.star[7:8]+'星'
        return render(request, 'index.html', locals())
    elif search_str == '4星':
        comments=CommentStar.objects.filter(star='allstar40 rating')
        for comment in comments:
            comment.star=comment.star[7:8]+'星'
        return render(request, 'index.html', locals())
    elif search_str == '5星':
        comments=CommentStar.objects.filter(star='allstar50 rating')
        for comment in comments:
            comment.star=comment.star[7:8]+'星'
        return render(request, 'index.html', locals())