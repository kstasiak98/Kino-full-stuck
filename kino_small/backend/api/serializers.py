from rest_framework import serializers
from backend.models import (Film, Seans, Sall, Ticket)


class FilmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Film
        fields = "__all__"


class SeansSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seans
        fields = "__all__"


class SallSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sall
        fields = "__all__"


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = "__all__"

