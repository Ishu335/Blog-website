from django.shortcuts import HttpResponse, render
from django.http import Http404,HttpResponseNotFound
from .models import Post

blogs = [
    {
        "id": 1,
        "title": "Getting Started with Python",
        "author": "Ishwar Sonawane",
        "category": "Programming",
        "likes": 120,
        "content": "This blog introduces Python programming, covering installation, syntax, and essential concepts like variables, loops, and functions for beginners."
    },
    {
        "id": 2,
        "title": "Top 10 Data Visualization Libraries",
        "author": "Neha Sharma",
        "category": "Data Science",
        "likes": 95,
        "content": "Explore the top 10 libraries for creating data visualizations in Python, including Matplotlib, Seaborn, Plotly, and Bokeh, with examples and use cases."
    },
    {
        "id": 3,
        "title": "Mastering FastAPI for Backend Development",
        "author": "Amit Verma",
        "category": "Web Development",
        "likes": 150,
        "content": "Learn how to build high-performance APIs using FastAPI. This guide covers routing, Pydantic models, authentication, and database integration."
    },
    {
        "id": 4,
        "title": "Understanding Docker and Containers",
        "author": "Ravi Patel",
        "category": "DevOps",
        "likes": 80,
        "content": "Get a clear understanding of Docker and containerization, including creating images, managing containers, and integrating Docker into development workflows."
    },
    {
        "id": 5,
        "title": "Machine Learning Basics Explained",
        "author": "Ishwar Sonawane",
        "category": "AI & ML",
        "likes": 210,
        "content": "An easy-to-follow introduction to machine learning concepts, covering supervised vs unsupervised learning, key algorithms, and practical implementation steps."
    }
]
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
    post_dict=[]
    for post in blogs:
        if post["id"]==id:
            post_dict=post
            break
    if post_dict:
        return render(request,'posts/post.html',{'post':post_dict})
    else:
        # return HttpResponseNotFound("Post is Not Found")
        raise Http404("templates\404.html")

def global_page(request):
    return render(request,'global_temp.html')


    