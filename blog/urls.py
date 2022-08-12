from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name="post_list"),
    path('<str:author>/<str:title>', views.post_info, name="post_info")
]
