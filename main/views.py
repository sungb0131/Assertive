import json
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Fee, CommunityPost, Convenient, Comment, Board, Parking

class Plans:
    def __init__(self, date, title):
        self.date = date
        self.content = title

def index(request):
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, 'index.html', {'plans': [
        ((Calender.date-timedelta(days=3),week[r-3]), '후라이드'), 
        ((Calender.date-timedelta(days=2),week[r-2]), '양념'), 
        ((Calender.date-timedelta(days=1),week[r-1]), '간장'), 
        ((Calender.date,week[r]), '뿌링클'),
        ((Calender.date+timedelta(days=1),week[r-6]), '굽네'), 
        ((Calender.date+timedelta(days=2),week[r-5]), '지코바'), 
        ((Calender.date+timedelta(days=1),week[r-4]), '눈꽃치즈')
    ], 'notices': CommunityPost.objects.filter(board=1).order_by('-date')[:5]})
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

def board_list(request, board_id):
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, 'list.html', {
        'board_list': CommunityPost.objects.filter(board=board_id).order_by('-date'),
        'board_type': Board.objects.get(id=board_id)
    })

def add_comment(request, post_id):
    if not request.user.is_authenticated:
        return redirect('/')
    post = get_object_or_404(CommunityPost, pk=post_id)
    comment = Comment(
        post=post,
        auther=request.user,
        contents=request.POST['comment'],
        date=timezone.now()
    )
    comment.save()
    return redirect(f'/main/board/{post_id}')

def view_post(request, post_id):
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, 'view.html', {
        'board': CommunityPost.objects.get(id=post_id),
        'comment': Comment.objects.filter(post_id=post_id).order_by('-date')
    })

def conv(request):
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, 'conv.html', {'contents': Convenient.objects.all()})

def write(request, board_id):
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, 'write.html', {'board_id': board_id})

def write_post(request, board_id):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        post = CommunityPost(
            board=Board.objects.get(id=board_id),
            auther=request.user,
            title=request.POST['postname'],
            contents=request.POST['contents'],
            date=timezone.now(),
            isAnonymous=request.POST.get('anonymous')=='y'
        )
        post.save()
        return redirect(f'/main/board/list/{board_id}')

def parking(request):
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, 'parking.html', {'levels': Parking.objects.all()})
