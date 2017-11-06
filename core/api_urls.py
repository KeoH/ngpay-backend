
from django.conf.urls import url, include
from rest_framework import routers

from transactions.views import TransactionViewSet

router = routers.DefaultRouter()

router.register(r'transaction', TransactionViewSet)

urlpatterns = router.urls
