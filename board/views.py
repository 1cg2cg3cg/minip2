from datetime import datetime
# from minip2.board.models import Boardcontent
from django.http.response import JsonResponse
from .models import Boardcontent, Reply, Rereply, User, Board
from django.shortcuts import render
from django.http import HttpResponse
import django.utils.crypto as crypt
import bcrypt
from django.utils import timezone

# Create your views here.

def index(request) :
    d=rereply(replyid_id=1,cre_date=timezone.datetime.now(),rereply='''대댓글입니다3''',userid_id=6)
    d.save()
    return HttpResponse('오류가 안뜨면 저장이 완료된것')

def test(request) :


    return render(request,'load.html')
    #return render(request,'test.html', {'a':12})

def load(request) :

    board_list = Boardcontent.objects.order_by('cre_date')
    
    return render(request, 'load.html', {'board_list' : board_list })
