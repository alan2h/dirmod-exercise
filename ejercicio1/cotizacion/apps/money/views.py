
import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view()
def money(request, money):
    """
    ---
       api para realizar la busqueda de la moneda

       @money = (str)
    ---
    """
    result = search_data(money)
    if result:
        return Response(result, status=status.HTTP_200_OK)
    return Response(result, status=status.HTTP_404_NOT_FOUND)


def search_data(money):

    """
       realiza la busqueda dentro del json Monedas
       parametros:
            money(str): nombre de la moneda 
    """

    json_file = open('moneys.json')
    data = json.load(json_file)
    result = {}
    for element in data:
        if element['money'] == money:
            result = element
    return result
