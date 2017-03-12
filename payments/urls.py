
from django.conf.urls import url

from .api import ListPayments

urlpatterns = [
    url(r'$', ListPayments.as_view())

]
