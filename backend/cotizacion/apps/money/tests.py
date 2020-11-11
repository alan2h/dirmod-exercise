
from rest_framework.test import APITestCase
from rest_framework import status


class moneyTestCase(APITestCase):

    url = '/cotizacion/'

    def test_money_valid(self):

        response = self.client.get(f'{self.url}dolar/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_money_invalid(self):

        response = self.client.get(f'{self.url}bad/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
