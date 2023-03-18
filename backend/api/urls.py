from django.urls import path
from . import views


urlpatterns = [
    path('user/', views.UserAPIView.as_view()),
    path('user_lang/', views.GetUserInfoAPIView.as_view()),
    path('liga/', views.LigaAPIView.as_view()),
    path('liga_table/', views.LigaTableAPIView.as_view()),
    path('liga_player/', views.LigaPlayerAPIView.as_view()),
    path('top_team/', views.TopTeamAPIView.as_view()),
    path('liga_calendar/', views.LigaCalendarAPIView.as_view()),
]


