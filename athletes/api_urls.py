# -*- coding: utf-8 -*-

from rest_framework.routers import SimpleRouter, Route
from athletes.api import AthletesViewSet, AthletesResultsViewSet

class AthletesRouter(SimpleRouter):
    routes = [
        Route(
            url=r'^{prefix}/$',
            mapping={'get': 'list'},
            name='{basename}-list',
            initkwargs={'suffix': 'List'}
        ),
        Route(
            url=r'^{prefix}/{lookup}/$',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            initkwargs={'suffix': 'Detail'}
        )
    ]

router = AthletesRouter()
router.register(r'athletes', AthletesViewSet)
router.register('athletes/(?P<object_pk>.+)/results', AthletesResultsViewSet, base_name='athletes_results')


urlpatterns = router.urls
