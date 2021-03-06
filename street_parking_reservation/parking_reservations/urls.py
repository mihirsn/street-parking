from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^api/v1/spots/$',
        views.add_parking_spots,
        name='add_parking_spots',
    ),
    url(
        r'^api/v1/available/spots/$',
        views.get_all_available_spots,
        name='get_all_available_spots',
    ),
    url(
        r'^api/v1/reserved/spots/$',
        views.get_all_reserved_spots,
        name='get_all_reserved_spots',
    ),
    url(
        r'^api/v1/reserve/spot/$',
        views.reserve_a_spot,
        name='reserve_a_spot',
    ),
    url(
        r'^api/v1/cancel/spot/$',
        views.cancel_a_spot,
        name='cancel_a_spot',
    ),
    url(
        r'^api/v1/show/cost/$',
        views.show_cost,
        name='show_cost',
    ),
    url(
        r'^api/v1/radius/spots/$',
        views.get_spots_by_radius,
        name='get_spots_by_radius',
    ),
]
