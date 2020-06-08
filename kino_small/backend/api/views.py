from rest_framework import generics
from backend.models import Film, Seans, Sall, Ticket

from backend.api.permissions import IsAdminUserOrReadOnly
from backend.api.serializers import FilmSerializer, SeansSerializer, SallSerializer,TicketSerializer


class FilmListCreateAPIView(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class FilmDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class SeansListCreateAPIView(generics.ListCreateAPIView):
    queryset = Seans.objects.all()
    serializer_class = SeansSerializer


class SallDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sall.objects.all()
    serializer_class = SallSerializer


class TicketListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer








