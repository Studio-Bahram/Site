from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Post, Instruction

def post(request, post_id):
    return HttpResponse("You're looking at question %s." % post_id)



'''
def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render({},request))

def posts(request):
    latest_post_list = Post.objects.order_by('-date_crate')[:5]
    template = loader.get_template('posts.html')
    context = {'latest_post_list': latest_post_list}    
    return HttpResponse(template.render(context, request))
    
def error_404(request,exception):
    template = loader.get_template("errors/404.html")
    return HttpResponse(template.render({},request))
def error_500(request):
    template = loader.get_template("errors/500.html")
    return HttpResponse(template.render({},request))⏎ 
'''