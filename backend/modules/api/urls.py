from django.urls import include, path
from rest_framework import routers

from api.views import ItemViewSet, ResultViewSet, EndpointViewSet, ClientViewSet, ConsoleViewSet, \
    ModelerViewSet, QuestionViewSet, ImplementationViewSet, DomainViewSet, IntegrationViewSet

router = routers.DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'results', ResultViewSet)
router.register(r'endpoints', EndpointViewSet)
router.register(r'clients', ClientViewSet, basename='Client')
router.register(r'consoles', ConsoleViewSet)
router.register(r'modelers', ModelerViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'implementations', ImplementationViewSet)
router.register(r'integrations', IntegrationViewSet)
router.register(r'domains', DomainViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
