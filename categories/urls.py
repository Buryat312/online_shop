from rest_framework.routers import SimpleRouter

from categories.views import CategoryViewSet

router = SimpleRouter()

router.register('categories', CategoryViewSet)

urlpatterns = []

urlpatterns += router.urls
