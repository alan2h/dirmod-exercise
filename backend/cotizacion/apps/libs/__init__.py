import json


def format_name(name_currency):

    """
    formatear el nombre de la moneda,
    al formato que recibe la api
    """

    file_json = open('moneys.json')
    data = json.load(file_json) 
    file_json.close()
    name_format = ''
    for element in data:
        if element['money'] == name_currency: # si el nombre esta en el json
            name_format = element['key'] # retorno como recibe la api
    return name_format


def get_all_currency_json():

    """
    devuelve todos las monedas dentro del json
    """
    file_json = open('moneys.json')
    data = json.load(file_json) 
    file_json.close()
    return data