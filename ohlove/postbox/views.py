from django.shortcuts import render,render_to_response,redirect
from django.views.decorators.csrf import csrf_exempt
from datetime import date,datetime,timedelta
from django.http import HttpResponse
from postbox.models import post
from random import randint
import simplejson as json
import os

def lastest_post(request):
	p = post.objects.all().order_by('-datetime').first()
	if p == None:
		p = post(datetime=datetime.now(),weekday=get_weekday(datetime.now().today().weekday()),content="Nonthing")
	return render_to_response("content.html",{"post":p})

@csrf_exempt
def today_post(request):
	d = date.today()
	p = get_post(d)
	if p:
		return HttpResponse(p.to_json())
	else:
		return HttpResponse(json.dumps({"result":"None"}))

@csrf_exempt
def older_post(request,ndate):
	date_list = ndate.split('-')
	if(len(date_list)==3):
		d = datetime(int(date_list[0]),int(date_list[1]),int(date_list[2]))
		p = post.objects.filter(datetime__lte=d).first()
		if p:
			return HttpResponse(p.to_json())
		else:
			return HttpResponse(json.dumps({'result':'None'}))
	else:
		return HttpResponse(json.dumps({'result':"Fail"}))

@csrf_exempt
def random_post(request,pid):
	if pid == 'None':
		posts = post.objects.filter()
	else:
		posts = post.objects.filter(id__ne=str(pid))
	length = len(posts)
	if length > 0:
		random_num = randint(0,length-1)
		return HttpResponse(posts[random_num].to_json())
	else:
		return HttpResponse(json.dumps({'result':'None'}))

def validate_user(request,password):
	return HttpResponse("success")

def index(request):
	return render_to_response("index.html")

@csrf_exempt
def write(request):
	if request.method== 'GET':
		return render_to_response("editor.html")
	else:
		content = request.POST.get('content')
		d = datetime.now()
		p = get_post(d.today())
		if p is not None:
			p.delete()
		post(datetime=d,weekday=get_weekday(d.today().weekday()),content=content).save()
		return HttpResponse(json.dumps({'result':'success'}))
	


def get_weekday(number):
	week = {6:'Sunday',0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday'}
	return week[number]

def get_post(today):
	dt_start = datetime(today.year,today.month,today.day)
	dt_end = datetime(today.year,today.month,today.day,23,59,59)
	posts = post.objects.filter(datetime__lte=dt_end,datetime__gte=dt_start)
	if(len(posts)==1):
		return posts[0]
	else:
		return None
		
