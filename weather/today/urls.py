# from django.urls import path
# from .views import weather
#
# urlpatterns = [
#     # other URL patterns
#     path('', weather),
# ]


from django.urls import path
from . import views
from django.views.generic import TemplateView



urlpatterns = [
    path('', TemplateView.as_view(template_name='today/weather.html'),
         name='home'),
    path('create/', views.weather, name='weather'),
    path('history/', views.HistoryWeatherView.as_view(), name='attempts'),
    path('delete/<int:pk>/', views.DeleteWeatherView.as_view(), name='delete_weather'),
]
