import json
from django.shortcuts import render
from datetime import datetime

from .models import Fee

class Plans:
    def __init__(self, date, title):
        self.date = date
        self.content = title
def index(request):
    
    return render(request, 'index2.html', {'plans': [
        Plans('12/4 (일)', '후라이드치킨먹기'), Plans('12/5 (월)', '양념치킨먹기'), Plans('12/6 (화)', '간장치킨먹기'), Plans('12/7 (수)', '뿌링클치킨먹기'),
        Plans('12/8 (목)', '굽네치킨먹기'), Plans('12/9 (금)', '지코바치킨먹기'), Plans('12/10 (토)', '눈꽃치즈치킨먹기')
    ]})

def graph(request, time, kind):
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
            "label": "작년",
            "data": [fee[i].fee for i in range(len(fee))]
        })
    return render(request, 'graph.html', {'chart_data': json.dumps(data)})