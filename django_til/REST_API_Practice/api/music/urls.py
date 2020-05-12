from django.urls import path
from . import views

urlpatterns = [
    path('artists/',views.Artists),
    path('artists/<int:artist_pk>/',views.ArtistsDetail),
    path('musics/', views.Musics),
    path('musics/<int:music_pk>/', views.MusicDetail),
    path('musics/<int:music_pk>/comments/', views.comment_create),
    path('comments/<int:comment_pk>/', views.comment_edit)

]

