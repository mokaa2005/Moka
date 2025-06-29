from django.shortcuts import render
from django.http import HttpResponse

from .models import post

def moarefi(request):
    #body
    return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")


def man(request):
    return HttpResponse("<h3>daram django yad migiram va gharare inja piade sazi konam</h3>")

def post_list(request):
    posts=post.objects.all()
    context={'posts':posts}
    return render(request,'posts/post_list.html',context=context)