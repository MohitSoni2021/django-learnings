from django.http import HttpResponse

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
