from django.urls import path
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bookmain/<int:id>', views.bookmain, name='bookmain'),
    path('letter/<str:title>/<int:id>', views.letter, name="letter"),
]