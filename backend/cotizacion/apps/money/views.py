
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .services import search_currency


@api_view()
def money(request, currency):
    """
    ---
       api para realizar la busqueda de la moneda

       @currency = (str)
    ---
    """
    result = search_currency(currency)
    data   = {'moneda': currency, 'precio': result['response']['result']['value']}
    state = status.HTTP_404_NOT_FOUND
    if result['status'] == 200: 
        state = status.HTTP_200_OK
    return Response(data, status=state) 
