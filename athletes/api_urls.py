# -*- coding: utf-8 -*-

from rest_framework.routers import SimpleRouter
from athletes.api import AthletesViewSet

router = SimpleRouter()

router.register(r'athletes', AthletesViewSet, base_name='athletes')

urlpatterns = router.urls