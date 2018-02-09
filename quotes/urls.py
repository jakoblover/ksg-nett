from django.urls import path

from quotes import views

urlpatterns = [
    path('<int:quote_id>/vote-up', views.vote_up),
    path('', views.list_view),
]
