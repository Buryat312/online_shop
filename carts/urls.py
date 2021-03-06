from rest_framework.routers import SimpleRouter

from carts.views import CartViewSet

router = SimpleRouter()

router.register('carts', CartViewSet)

urlpatterns = []

urlpatterns += router.urls
