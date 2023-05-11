from django.urls import path

from . import views

urlpatterns = [
    #path('',views.movies_list.as_view()),
    path('',views.movies_detail.as_view()),

]
