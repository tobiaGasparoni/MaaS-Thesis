import uuid
from django.db import models
from djongo.models import JSONField


class Item(models.Model):
    ID = models.CharField(max_length=100, primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    name = models.CharField(max_length=60)
    age = models.IntegerField()
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)

    def __str__(self):
        return "{}, {} years old".format(self.name, str(self.age))


class Client(models.Model):
    # Client's email
    ID = models.CharField(max_length=100, primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    email = models.EmailField(max_length=254, editable=True, unique=True)
    name = models.CharField(max_length=200, null=False)

    def __str__(self):
        return "{}: {}".format(self.name, self.email)


class Modeler(models.Model):
    # Client's email
    ID = models.CharField(max_length=100, primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    email = models.EmailField(max_length=254, editable=True, unique=True)
    name = models.CharField(max_length=200, null=False)
    clients = models.ManyToManyField(Client, blank=True)

    def __str__(self):
        return "{}: {}".format(self.name, self.email)


class Domain(models.Model):
    ID = models.CharField(max_length=100, primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    name = models.CharField(max_length=1000, unique=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    ID = models.CharField(max_length=100, primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    modeler = models.ForeignKey(Modeler, on_delete=models.CASCADE)
    question = models.CharField(max_length=1000)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    data = JSONField(True, default={}, null=False)

    def __str__(self):
        return self.question


class Implementation(models.Model):
    ID = models.CharField(max_length=100, primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    questions = models.ManyToManyField(Question, blank=True)
    modeler = models.ForeignKey(Modeler, related_name="implementation_creator", on_delete=models.CASCADE)
    name = models.CharField(max_length=1000, null=False)

    def __str__(self):
        return self.name


class Integration(models.Model):
    ID = models.CharField(max_length=100, primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    modeler = models.ForeignKey(Modeler, related_name="integration_creator", on_delete=models.CASCADE)
    name = models.CharField(max_length=1000, null=False, unique=True)

    def __str__(self):
        return self.name


class Console(models.Model):
    ID = models.CharField(max_length=100, primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    name = models.CharField(max_length=500)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    modeler = models.ForeignKey(Modeler, on_delete=models.CASCADE)
    integration = models.ForeignKey(Integration, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Endpoint(models.Model):
    ID = models.CharField(max_length=100, primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    name = models.CharField(max_length=1000, unique=True)
    console = models.ForeignKey(Console, on_delete=models.CASCADE)
    answers = JSONField(True, default={}, null=False)

    def __str__(self):
        return self.name


class Result(models.Model):
    ID = models.CharField(max_length=100, primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    input = JSONField(True, default={}, null=False)
    output = JSONField(True, default={}, null=False)
    endpoint = models.ForeignKey(Endpoint, on_delete=models.CASCADE)

    def __str__(self):
        return self.ID
