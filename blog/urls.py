
from django.urls import path

from . import views # dot if from the same folder


app_name = 'blog'

urlpatterns = [
   # name to link {% %} in the html templates
   path('',views.all_blogs, name='all_blogs'),
   
   # is there any path that is an int
   # blog_id is passed to the detail function in views.py
   path('<int:blog_id>/',views.detail, name='detail'), 
    
]
