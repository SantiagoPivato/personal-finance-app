from django.db import models

# Create your models here.
class Unit(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, blank=True)
    symbol = models.CharField(max_length=10)

    def __str__(self):
        if(self.symbol == self.code):
            return str(self.name) + " (" +  str(self.code) + ")"    
        return str(self.name) + " (" +  str(self.code) + str(self.symbol) + ")"
    
    class Meta:
        verbose_name = "Unit"
        verbose_name_plural = "Units"

class Variable(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    source = models.CharField(max_length=200)
    unit = models.ForeignKey(Unit, on_delete=models.RESTRICT)
    external_reference = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

class VariableValue(models.Model):
    variable = models.ForeignKey(Variable, on_delete=models.RESTRICT)
    value = models.DecimalField(max_digits=22, decimal_places=10)
    datetime = models.DateTimeField()