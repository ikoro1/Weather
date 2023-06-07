from django.urls import path, include
from django.views.generic import TemplateView

app_name = 'weather'  # Add this line if you haven't already

urlpatterns = [
    path('', TemplateView.as_view(template_name='today/weather.html'), name='home'),
    path('weather/', include('today.urls')),
]
