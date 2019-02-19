from rest_framework import routers
from meadows import views

router = routers.SimpleRouter()

router.register(
    r'',
    views.MeadowViewSet
)

urlpatterns = router.urls
