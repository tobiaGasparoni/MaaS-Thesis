
from rest_framework import serializers
from rest_framework.fields import ChoiceField

from api.models import Client, Endpoint, Implementation, Console, Item, Modeler, Question, Result, Domain, Integration


"""
BEGIN Auxiliary serializers
"""


class JSONSerializerField(serializers.Field):
    """ Serializer for JSONField -- required to make field writable"""
    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        return value


"""
END Auxiliary serializers
"""


class ModelerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Modeler
        fields = ('ID', 'email', 'name', 'clients')


class ClientSerializer(serializers.ModelSerializer):

    modelers = ModelerSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ('ID', 'email', 'name', 'modelers')


class EndpointSerializer(serializers.ModelSerializer):

    answers = JSONSerializerField()

    class Meta:
        model = Endpoint
        fields = ('ID', 'name', 'console', 'answers')


class ConsoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Console
        fields = ('ID', 'name', 'client', 'modeler', 'integration')


class IntegrationSerializer(serializers.ModelSerializer):

    '''
    def create(self, validated_data):
        
        modeler = Modeler.objects.filter(email=validated_data['modeler'])['ID']
        validated_data['modeler'] = modeler

        return super().create(**validated_data)
    '''
    class Meta:
        model = Integration
        fields = ('ID', 'name', 'modeler')


class ImplementationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Implementation
        fields = ('ID', 'questions', 'modeler', 'name')


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('ID', 'name', 'age')


class DomainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Domain
        fields = ('ID', 'name')


class QuestionSerializer(serializers.ModelSerializer):

    data = JSONSerializerField()
    implementations = ModelerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('ID', 'domain', 'modeler', 'question', 'data', 'implementations')


class ResultSerializer(serializers.ModelSerializer):

    input = JSONSerializerField()
    output = JSONSerializerField()

    class Meta:
        model = Result
        fields = ('ID', 'endpoint', 'input', 'output')
