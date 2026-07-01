# It is used to handle the http requests...
from django.http import HttpResponse

# It is used to handle the rendering of the templetes...
from django.shortcuts import render

# Create your views here.
# by defalt view have one parameter whih is the request...
def blogHome(request):
    print(request)
    return HttpResponse("This is the home of the blog...")

def blog_post_1(request):
    return HttpResponse("This is post 1")

def blog_post_2(request):
    return HttpResponse("This is post 2")

# defining the dynamic urls...
def blog_post(req, post_id):
    return HttpResponse(f"This is post {post_id}")

def blogTemplete(req):
    # for sending the data to the templete:
    context = {
        'variable': 'variable',
        'name': 'Mohit Soni',
        'skills' : ['reactjs', 'nextjs', 'tailwind', 'django', 'nodejs', 'expressjs'],
        'blog' : {
            'title' : 'Title of the blog',
            'author' : 'Mohit Soni', 
            'content' : '<b>This is the content of the blog. by mohit soni.</b>'
        },
        "comments" : None
    }
    return render(req, 'blogs.html', context)


