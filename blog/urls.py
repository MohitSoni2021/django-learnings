from django.urls import path
from blog import views
urlpatterns = [
    path("", views.blogTemplete, name="bloghome"),
    path('<int:post_id>', views.blog_post, name="blog_post")
]
