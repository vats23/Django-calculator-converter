from django.urls import path,include
from . import views
app_name = 'calculator'

urlpatterns=[
    path('',views.index,name='indexi'),
]
