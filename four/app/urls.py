from django.urls import path
from app import views

#template tagging
app_name = 'app'

urlpatterns =[
    path('relative/',views.relative, name='relative'),
    path('other/', views.other,name='other'),
]
