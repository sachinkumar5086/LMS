from django.urls import path
from . import views

urlpatterns=[
    path('index/',views.index),
    path('',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('facility/',views.facility),
    path('feedback/',views.feedback),
    path('signin/',views.signin),
    path('successstory/',views.successstory),
    path('batches/',views.mynewbatches),
    path('signup/',views.registration),


]
