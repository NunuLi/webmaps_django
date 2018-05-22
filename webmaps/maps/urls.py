from django.urls import path
from . import views
from django.urls import include, path

app_name = 'maps'
urlpatterns = [
	path('<int:app_id>/', views.detail, name='detail'),
]