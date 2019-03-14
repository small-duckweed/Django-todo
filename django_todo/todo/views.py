from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse   # 类似前端模版语言  url 函数
from django.views import generic    # 从数据库取数据前台渲染列表的操作比较简单重复，django封装了这个过程提供统一的模版
from .models import Content
from datetime import datetime

def index(request):

    content = Content.objects.all().order_by('text')
    context = {
        "content": content
    }
    return render(request, 'todo/index.html', context)

def particulars(request,content_id):
    print(content_id)
    content = Content.objects.get(id=content_id)
    print(content.id)
    context = {
        'content': content
    }
    return render(request, 'todo/particulars.html/', context)

def redirect(request,question_id):
    c = Content.objects.get(id=question_id)
    c.status = 1
    c.save()
    return HttpResponseRedirect(reverse('todo:index',))

def add(request):
    text = request.POST['content']
    # print(text)
    q = Content(text=text, issue_date=datetime.now(), status=0, finish_date=None)
    q.save()
    return HttpResponseRedirect(reverse('todo:index'))


def delete(request, content_id):
    print(content_id)
    c = Content.objects.filter(id=content_id)
    c.delete()
    return HttpResponseRedirect(reverse('todo:index'))