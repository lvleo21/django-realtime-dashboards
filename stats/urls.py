from django.urls import path
from stats import views

app_name = "stats"
urlpatterns = [
    path('', views.StatisticListView.as_view(), name="statistics"),
    path('create', views.StatisticCreateView.as_view(), name="statistic_add"),
    path('<slug>', views.Dashboard.as_view(), name="dashboard"),

]