from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:question_id>/', views.detail, name='detail'),
    path('results/', views.results, name='results'),
    path('<int:question_id>/answer/<person_id>', views.answer, name='answer'),
    path('finish/', views.finish, name='finish')
]