from django.conf.urls import url
from . import views


urlpatterns = [
    # url(
    #     r'^api/v1/users/(?P<pk>[0-9]+)$',
    #     views.get_delete_update_user,
    #     name='get_delete_update_user'
    # ),
    url(
        r'^api/v1/users/$',
        views.get_post_users,
        name='get_post_users'
    )
]
