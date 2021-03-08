from django.urls import path

from . import views

app_name = "poll"
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('detail', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('results', views.results, name='results'),

]