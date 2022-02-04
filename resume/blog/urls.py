from django.urls import path
from . import views 

app_name = 'blog'

urlpatterns = [
    path('',views.all_blog,name="all_blog")
]