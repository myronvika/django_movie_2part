from django.db import models
from rest_framework import generics, permissions, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import Movie, Actor, Review
from .serializers import (
    MovieListSerializer,
    MovieDetailSerializer,
    ReviewCreateSerializer,
    CreateRatingSerializer,
    ActorListSerializer,
    ActorDetailSerializer,
)
from .service import get_client_ip, MovieFilter, PaginationMovies


class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    """Вивід списку фільмів"""
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MovieFilter
    pagination_class = PaginationMovies

    def get_queryset(self):
        movies = Movie.objects.filter(draft=False).annotate(
            rating_user=models.Count("ratings",
                                     filter=models.Q(ratings__ip=get_client_ip(self.request)))
        ).annotate(
            middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
        )
        return movies

    def get_serializer_class(self):
        if self.action == 'list':
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieDetailSerializer


class ReviewCreateViewSet(viewsets.ModelViewSet):
    """Добавлення відгука до фільму"""
    serializer_class = ReviewCreateSerializer


class AddStarRatingViewSet(viewsets.ModelViewSet):
    """Добавлення рейтингу до фільму"""
    serializer_class = CreateRatingSerializer

    def perform_create(self, serializer):
        serializer.save(ip=get_client_ip(self.request))


class ActorsViewSet(viewsets.ReadOnlyModelViewSet):
    """Вивід акторів і режисерів"""
    queryset = Actor.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ActorListSerializer
        elif self.action == "retrieve":
            return ActorDetailSerializer


# class MovieListView(generics.ListAPIView):
#     """Вивід списку фільмів"""
#     serializer_class = MovieListSerializer
#     filter_backends = (DjangoFilterBackend,)
#     filterset_class = MovieFilter
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get_queryset(self):
#         movies = Movie.objects.filter(draft=False).annotate(
#             rating_user=models.Count("ratings",
#                                      filter=models.Q(ratings__ip=get_client_ip(self.request)))
#         ).annotate(
#             middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
#         )
#         return movies

#
# class MovieDetailView(generics.RetrieveAPIView):
#     """Вивід фільма"""
#     queryset = Movie.objects.filter(draft=False)
#     serializer_class = MovieDetailSerializer


# class ReviewCreateView(generics.CreateAPIView):
#     """Добавлення відгука до фільму"""
#     serializer_class = ReviewCreateSerializer


# class AddStarRatingView(generics.CreateAPIView):
#     """Добавлення рейтинга до фільму"""
#     serializer_class = CreateRatingSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(ip=get_client_ip(self.request))


# class ActorsListView(generics.ListAPIView):
#     """Вивід списку акторів"""
#     queryset = Actor.objects.all()
#     serializer_class = ActorListSerializer
#
#
# class ActorsDetailView(generics.RetrieveAPIView):
#     """Вивід актора і режисера"""
#     queryset = Actor.objects.all()
#     serializer_class = ActorDetailSerializer

