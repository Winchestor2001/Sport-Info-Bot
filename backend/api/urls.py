from django.urls import path
from . import views


urlpatterns = [
    path('user/', views.UserAPIView.as_view())
]


