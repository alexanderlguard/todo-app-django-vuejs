from rest_framework import routers
from .viewsets import GroupViewSet, TaskViewSet

router = routers.SimpleRouter()
router.register('groups', GroupViewSet)
router.register('tasks', TaskViewSet)

urlpatterns = router.urls