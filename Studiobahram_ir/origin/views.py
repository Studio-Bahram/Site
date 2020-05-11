from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.http import require_POST

from .models import Post

@csrf_exempt
@require_POST
def post_api(request):
    post_vs = request.POST.keys()
    if "token" in post_vs:
        token = request.POST["token"]
        if token == "1234":
            return JsonResponse({"!":"@"})
        else:
            return JsonResponse({"error":"not match token"})
    else:
        return JsonResponse({"error":"pls send token"})

'''
this_user = get_object_or_404(User, token__token=this_token)
'''
# def post_tag(request, post_tag):
#     try:
#         post_filter_by_tag = Post.objects.filter(tag=post_tag)
#         this_post = post_filter_by_tag[0]
#         context = {"post":this_post,"post_tag":post_tag}
#         template = loader.get_template('post.html')
#         return HttpResponse(template.render(context, request))
#     except IndexError:
#         return HttpResponse("404")
#     except Exception as err:
#         return HttpResponse(str(err))
    

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