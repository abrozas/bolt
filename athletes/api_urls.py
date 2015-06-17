# -*- coding: utf-8 -*-

from rest_framework.routers import SimpleRouter
from athletes.api import AthletesViewSet

router = SimpleRouter()

router.register('athletes', AthletesViewSet, base_name='athletes')

urlpatterns = router.urls