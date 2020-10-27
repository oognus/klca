from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='layout_index'),
]