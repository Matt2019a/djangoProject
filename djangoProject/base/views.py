from django.shortcuts import render
from django.http import HttpResponse
from base.models import Activity
import json
from django.core import serializers
from . import froms


def home(request):
    return HttpResponse('Home page')


def activity(request):
    return HttpResponse('Activity')


def activities(request):
    activityList = Activity.objects.order_by('date')
    res = serializers.serialize("json", activityList)

    date_dict = {'activityList': res}
    print(date_dict)
    return HttpResponse(json.dumps(date_dict))


def getActivities(request):
    key = json.loads(request.body)["keyword"]
    activityList = Activity.objects.filter(title__icontains=key)
    res = serializers.serialize("json", activityList)
    date_dict = {'activityList': res}

    s1 = json.dumps(date_dict, ensure_ascii=False)
    print(type(s1))
    print(s1)
    s1.replace('\\', '')
    print(s1)
    return HttpResponse(s1)
# Create your views here.
