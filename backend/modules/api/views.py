from rest_framework import viewsets, status

from api.models import Item, Client, Console, Endpoint, Implementation, Modeler, Question, Result, Domain, Integration
from api.serializers import ItemSerializer, ClientSerializer, ConsoleSerializer, EndpointSerializer, \
    ImplementationSerializer, ModelerSerializer, QuestionSerializer, ResultSerializer, DomainSerializer, \
    IntegrationSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from api.services.integrations import directory


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('name')
    serializer_class = ItemSerializer


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer

    # @action(detail=False, methods=['post'])
    def get_queryset(self):
        queryset = Client.objects.all()
        email = self.request.query_params.get('email')
        print(email)
        if email is not None:
            queryset = queryset.filter(email=email)
        return queryset


class ConsoleViewSet(viewsets.ModelViewSet):
    queryset = Console.objects.all().order_by('ID')
    serializer_class = ConsoleSerializer


class EndpointViewSet(viewsets.ModelViewSet):
    queryset = Endpoint.objects.all().order_by('ID')
    serializer_class = EndpointSerializer

    @action(detail=True, methods=['post'])
    def solve(self, request, pk=None):

        current_endpoint = Endpoint.objects.get(ID=pk)
        current_console = Console.objects.get(ID=current_endpoint.console.ID)
        current_integration = Integration.objects.get(ID=current_console.integration.ID)

        result = directory.solve(current_integration, current_endpoint.answers, request.data)

        Result.objects.create(input=request.data, output=result, endpoint=current_endpoint)

        return Response(result)


class ImplementationViewSet(viewsets.ModelViewSet):
    queryset = Implementation.objects.all().order_by('ID')
    serializer_class = ImplementationSerializer


class IntegrationViewSet(viewsets.ModelViewSet):
    queryset = Integration.objects.all().order_by('ID')
    serializer_class = IntegrationSerializer

    
class ModelerViewSet(viewsets.ModelViewSet):
    queryset = Modeler.objects.all().order_by('ID')
    serializer_class = ModelerSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('ID')
    serializer_class = QuestionSerializer


class DomainViewSet(viewsets.ModelViewSet):
    queryset = Domain.objects.all().order_by('ID')
    serializer_class = DomainSerializer


class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all().order_by('ID')
    serializer_class = ResultSerializer
