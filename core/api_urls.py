
from django.conf.urls import url, include



urlpatterns = [
    url(r'^operations', include('operations.urls'))
]
