from django.urls import path
from querysys.views import index,addstudent

urlpatterns = [
    path('index/', index),
    path('addstudent/', addstudent),

]
