from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    # 首页 http:/ip:port/polls/
    path('', views.index, name='index'),
    path('particulars/<int:content_id>/', views.particulars, name='particulars'),
    path('<int:question_id>/redirect/', views.redirect, name='redirect'),
    path('add/', views.add, name='add'),
    path('<int:content_id>/delete/', views.delete, name="delete")
]
