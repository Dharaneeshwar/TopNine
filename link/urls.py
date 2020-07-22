from django.urls import path
from . import views

urlpatterns=[

    path('Link/read/', views.withLink),
    path('Link/',views.link,name='link')

]