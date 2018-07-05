from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('api/pie', views.APIViewPie.as_view(), name='api-pie'),
    path('api/bar', views.APIViewBar.as_view(), name='api-bar'),

]
