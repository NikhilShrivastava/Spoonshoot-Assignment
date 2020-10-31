from django.conf.urls import url

from .views import *

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)


urlpatterns = [
    path('booksapi/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
