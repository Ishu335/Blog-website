from django.shortcuts import HttpResponse, render
from django.http import Http404,HttpResponseNotFound
from .models import Post

Categories=[
'Travel',
'Food',
'Place'
]
# Create your views here.
def home(request):
    all_post=Post.objects.all()
    return render(request,'posts/index.html',{'posts':all_post ,'Categories':Categories})

def post(request,id):
    try:
        post_id=Post.objects.get(id=id)    
    except :
        raise Http404("templates\404.html")
    return render(request,'posts/post.html',{'post':post_id})

def global_page(request):
    return render(request,'global_temp.html')


    