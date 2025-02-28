from django.shortcuts import render, HttpResponse
from .services import ApiEstadisticasCambiariasBCRA
from .models import Variable, Unit, VariableValue
from django.http import JsonResponse

from datetime import datetime

# Create your views here.

#Vista principal
def index(request):
    variables_bcra = list(Variable.objects.all())
    return render(request, "app/index.html", {"variables_bcra": variables_bcra})


#Obtiene y almacena las variables del BCRA en la tabla de Variables
def get_variables_bcra():
    #Api call
    api = ApiEstadisticasCambiariasBCRA()
    response = api.call("Monetarias", "GET")

    #Response validation
    if(api.last_status_code != 200 or response["status"] != 200):
        return response

    #Response OK
    for result in response["results"]:
        #Variable filtering
        if result["fecha"] < "2024-12-30" or result["categoria"] != 'Principales Variables': 
            continue

        #Skipping duplicates
        if(Variable.objects.filter(external_reference=result["idVariable"]).exists()):
            continue

        #Unit identifiaction
        code = "USD" if "dólares" in result["descripcion"] else "ARS"
        code = "%" if "%" in result["descripcion"] else code

        #Model insert
        variable = Variable(
            name = result["descripcion"][0:150],
            description = result["descripcion"],
            unit = Unit.objects.get(code = code),
            source = api.url,
            external_reference = result["idVariable"]
        )
        variable.save()


    variables = list(Variable.objects.filter())

    return variables





#Obtiene y almacena las variables del BCRA en la tabla de Variables
def get_variable_values_bcra(request, variable):
    #input
    today = datetime.today().strftime('%Y-%m-%d')
    fromdate = request.GET.get("from", today)
    todate = request.GET.get("to", today)

    #Input validation
    if fromdate > todate:
        return render(request, "app/error.html", {"error" : "From date must be lower than to date"})
    if(not Variable.objects.filter(id=variable).exists()):
        return render(request, "app/error.html", {"error" : "Invalid variable"})


    #Api call
    variable_object = Variable.objects.get(id=variable)
    endpoint = f"Monetarias/{str(variable_object.external_reference)}?desde={fromdate}&hasta={todate}" 

    api = ApiEstadisticasCambiariasBCRA()
    response = api.call(endpoint, "GET")

    #Response validation
    if(api.last_status_code != 200 or response["status"] != 200):
        return render(request, "app/error.html", {"error" : response})

    #Response OK
    for result in response["results"]:

        
        #Skipping duplicates
        if(VariableValue.objects.filter(variable=variable_object, datetime=result["fecha"]).exists()):
            continue

        #Model insert
        variable_value = VariableValue(
            variable = variable_object,
            value = result["valor"],
            datetime = result["fecha"],
        )
        variable_value.save()


    variable_values = list(VariableValue.objects.filter(variable = variable, datetime__gte=fromdate, datetime__lte=todate).order_by('datetime').values())
    return JsonResponse({"data": variable_values}) 


