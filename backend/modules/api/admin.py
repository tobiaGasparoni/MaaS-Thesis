from django.contrib import admin

# Register your models here.
from api.models import Item, Result, Endpoint, Client, Console, Modeler, Question, Implementation

admin.site.register(Item)
admin.site.register(Result)
admin.site.register(Endpoint)
admin.site.register(Client)
admin.site.register(Console)
admin.site.register(Modeler)
admin.site.register(Question)
admin.site.register(Implementation)
