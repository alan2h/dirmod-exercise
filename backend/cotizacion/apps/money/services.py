
import json
import requests

from django.conf import settings


def search_currency(currency):

    """
       realiza la busqueda dentro del json Monedas
       parametros:
            money(str): nombre de la moneda 
    """

    response = requests.get(f'https://api.cambio.today/v1/quotes/ARS/{currency}/json?quantity=1&key={ settings.SECRET_KEY_API }')
    return { 'response': response.json(), 'status': response.status_code }
