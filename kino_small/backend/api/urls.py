from django.urls import path
from backend.api.views import (FilmListCreateAPIView,
                               SeansListCreateAPIView,
                               SallDetailAPIView,
                               FilmDetailAPIView,
                               TicketListCreateAPIView)

urlpatterns = [
    path("films/",
         FilmListCreateAPIView.as_view(),
         name="film-list"),

    path("seans/",
         SeansListCreateAPIView.as_view(),
         name="seans-list"),

    path("films/<int:pk>/",
         FilmDetailAPIView.as_view(),
         name="film-detail"),

    path("ticket/",
         TicketListCreateAPIView.as_view(),
         name="tickets"),

    path("sall/<int:pk>/",
         SallDetailAPIView.as_view(),
         name="Sall-detail"),
]
