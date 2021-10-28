from rest_framework.routers import SimpleRouter

from orders.views import OrderListView

router = SimpleRouter()

router.register('orders', OrderListView)

urlpatterns = []

urlpatterns += router.urls
