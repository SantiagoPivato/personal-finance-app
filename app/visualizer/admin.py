from django.contrib import admin
from .models import Unit, Variable, VariableValue

# Register your models here.
class VariableAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', 'unit', 'external_reference') 


class VariableValueAdmin(admin.ModelAdmin):
    list_display = ('id', 'variable', 'value', 'datetime') 

admin.site.register(Unit)
admin.site.register(Variable, VariableAdmin)
admin.site.register(VariableValue, VariableValueAdmin)