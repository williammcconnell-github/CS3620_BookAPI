from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import BookData


# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.all()
    serializer_class = BookSerializer


class UncategorizedViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='uncategorized')
    serializer_class = BookSerializer


class ActionAdventureViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='action_adventure')
    serializer_class = BookSerializer


class ComicBookViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='comic_book')
    serializer_class = BookSerializer


class FantasyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='fantasy')
    serializer_class = BookSerializer


class RomanceViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='romance')
    serializer_class = BookSerializer


class ScienceFictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='science_fiction')
    serializer_class = BookSerializer


class MysteryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='mystery')
    serializer_class = BookSerializer


class HistoricalFictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='historical_fiction')
    serializer_class = BookSerializer


class ThrillerViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='thriller')
    serializer_class = BookSerializer


class NonFictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='non_fiction')
    serializer_class = BookSerializer
