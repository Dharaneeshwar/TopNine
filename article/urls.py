from django.urls import path
from . import views

urlpatterns=[

    path('/article1/', views.article1,name='a1'),
    path('/article2/', views.article2,name='a2'),
    path('/article3/', views.article3,name='a3'),
    path('/article4/', views.article4,name='a4'),
    path('/article5/', views.article5,name='a5'),
    path('/article6/', views.article6,name='a6'),
    path('/article7/', views.article7,name='a7'),
    path('/article8/', views.article8,name='a8'),
    path('/article9/', views.article9,name='a9'),
]