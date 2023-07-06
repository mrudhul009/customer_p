from django.urls import path,include
# from watchlist.api.views import movieli,movie_details
from watchlist.api.views import WatchlistAV,WatchdetailsAV,streamplatformAV,streamplatformdetailAV


urlpatterns = [
    path("list/",WatchlistAV.as_view(), name="list of movies" ),
    path('<int:pk>/',WatchdetailsAV.as_view(),name="choosen movie"),
    path('stream/',streamplatformAV.as_view(),name='stream'),
    path('stream/<int:pk>',streamplatformdetailAV.as_view(),name='stream details'),

]