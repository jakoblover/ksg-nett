from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views import UserViewSet
from quotes.views import QuoteViewSet, QuoteVoteViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'quotes', QuoteViewSet)
router.register(r'quote-votes', QuoteVoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
