from django.conf.urls import url, include
from django.views import generic
from accounts.views import AccountViewSet
from invoices.views import InvoiceViewSet
from lineitems.views import LineViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'invoices', InvoiceViewSet)
router.register(r'lineitems', LineViewSet)


# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^$', generic.RedirectView.as_view(
         url='/api/', permanent=False)),
    url(r'^api/$', get_schema_view()),
    url(r'^api/auth/', include(
        'rest_framework.urls', namespace='rest_framework')),
    url(r'^api/auth/token/obtain/$', TokenObtainPairView.as_view()),
    url(r'^api/auth/token/refresh/$', TokenRefreshView.as_view()),
]
