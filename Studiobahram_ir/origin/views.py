from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Post, Instruction

def post_id(request, post_id):
    try:
        if post_id > 0:
            post_filter_by_id = Post.objects.all()
            this_post = post_filter_by_id[post_id-1]
            context = {"post":this_post,"post_id":post_id}
            template = loader.get_template('post.html')
            return HttpResponse(template.render(context, request))
        else:
            return HttpResponse("404")
    except IndexError:
        return HttpResponse("404")
    except Exception as err:
        return HttpResponse(str(err))

def post_tag(request, post_tag):
    try:
        post_filter_by_tag = Post.objects.filter(tag=post_tag)
        this_post = post_filter_by_tag[0]
        context = {"post":this_post,"post_tag":post_tag}
        template = loader.get_template('post.html')
        return HttpResponse(template.render(context, request))
    except IndexError:
        return HttpResponse("404")
    except Exception as err:
        return HttpResponse(str(err))
    

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