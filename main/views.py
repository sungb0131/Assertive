import json
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Fee, CommunityPost, Convenient, Comment

class Plans:
    def __init__(self, date, title):
        self.date = date
        self.content = title

def index(request):
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, 'index.html', {'plans': [
        Plans('12/4 (일)', '후라이드치킨먹기'), Plans('12/5 (월)', '양념치킨먹기'), Plans('12/6 (화)', '간장치킨먹기'), Plans('12/7 (수)', '뿌링클치킨먹기'),
        Plans('12/8 (목)', '굽네치킨먹기'), Plans('12/9 (금)', '지코바치킨먹기'), Plans('12/10 (토)', '눈꽃치즈치킨먹기')
    ], 'notices': CommunityPost.objects.filter(board='notice').order_by('-date')[:5]})

def graph(request, time, kind):
    if not request.user.is_authenticated:
        return redirect('/')
    data = {
        "datasets":[],
        "labels": ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    }
    if time == 'prev' or time == 'both':
        fee = Fee.objects.filter(user=request.user, date_year=datetime.now().year-1, kind=kind).order_by('date_month')
        data['datasets'].append({
            "label": "작년",
            "data": [fee[i].fee for i in range(len(fee))]
        })
    if time == 'both' or time == 'now':
        fee = Fee.objects.filter(user=request.user, date_year=datetime.now().year, kind=kind).order_by('date_month')
        data['datasets'].append({
            "label": "올해",
            "data": [fee[i].fee for i in range(len(fee))]
        })
    type_dict = {"electric": "전기", "water": "수도", "gas": "가스", "waste": "음식물 쓰레기 처리비"}
    return render(request, 'graph.html', {'graph_type':type_dict[kind],'chart_data': json.dumps(data), 'time': time, 'type': kind})

def board_list(request):
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, 'list.html', {'board_list': CommunityPost.objects.all().order_by('-date')})

def add_comment(request, post_id):
    post = get_object_or_404(CommunityPost, pk=post_id)
    comment = Comment(
        post=post,
        auther=request.user,
        contents=request.POST['comment'],
        date=timezone.now()
    )
    comment.save()
    return redirect(f'/main/board/{post_id}')

def post(request, board_id):
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, 'view.html', {'board': CommunityPost.objects.get(id=board_id), 'comment': Comment.objects.filter(post_id=board_id).order_by('-date')})

def conv(request):
    return render(request, 'conv.html', {'contents': Convenient.objects.all()})