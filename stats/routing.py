from django.urls import path

from stats import consumers


websocket_urlpatterns = [
    path('ws/<slug:dashboard>/', consumers.DashboardConsumer.as_asgi()),
]