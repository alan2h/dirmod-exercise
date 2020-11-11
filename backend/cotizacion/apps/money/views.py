
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .services import search_currency
from apps.libs import format_name, get_all_currency_json


@api_view()
def money(request, currency):
    """
    ---
       api para realizar la busqueda de la moneda

       @currency = (str)
    ---
    """
    data   = {}
    name_format = format_name(currency) # formateo el nombre para la api
    if name_format:
        result = search_currency(name_format)
        data   = {'moneda': currency, 'precio': result['response']['result']['value']}
        return Response(data, status=status.HTTP_200_OK) 
    state = status.HTTP_404_NOT_FOUND
    return Response(data, status=state) 


@api_view()
def all_currency(request):
    """
    ---
       api para saber todas las monedas permitidas
    ---
    """
    return Response(get_all_currency_json(), status=status.HTTP_200_OK) 
