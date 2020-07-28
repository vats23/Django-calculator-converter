from django.urls import path
from . import views

app_name='converter'

urlpatterns =[
    path('bin/',views.indexbin,name='indexbin'),
    path('deci/',views.indexdeci,name='indexdeci')

]
