from django.conf.urls import url
from .views import *

urlpatterns = [
    # User related URLs
    url(r'add/user/', add_user),
    url(r'get/user/', get_user),

    # User Activity related URLs
    url(r'add/userActivity/', add_user_activity),
    url(r'get/userActivity/', get_user_activity),
]