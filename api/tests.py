from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Imovel, Anuncio, Reserva

class ImovelTests(APITestCase):
    def test_create_imovel_success(self):
        """
        Ensure we can create a new imovel object.
        """
        url = 'http://127.0.0.1:8000/imovel'
        data = {
            "max_hospedes": 3,
            "banheiros": 2,
            "pet": True,
            "limpeza": 150.50,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Imovel.objects.count(), 1)
        self.assertEqual(Imovel.objects.get().max_hospedes, 3)


    def test_create_imovel_fail(self):
        """
        Ensure we can't create a new imovel object using a bad payload.
        """
        url = 'http://127.0.0.1:8000/imovel'
        data = {
            "banheiros": 2,
            "pet": True,
            "limpeza": 150.50,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        

class AnuncioTests(APITestCase):
    def test_create_anuncio_success(self):
        """
        Ensure we can create a new anuncio object.
        """
        # creating imovel to use id
        url = 'http://127.0.0.1:8000/imovel'
        data = {
            "max_hospedes": 3,
            "banheiros": 2,
            "pet": True,
            "limpeza": 150.50,
        }
        self.client.post(url, data, format='json')

        url = 'http://127.0.0.1:8000/anuncio'
        data = {
            "imovel_id": Imovel.objects.get().id,
            "plataforma": "5A",
            "taxa_plataforma": 150.50
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_create_anuncio_fail(self):
        """
        Ensure we can't create a new anuncio object using a bad payload.
        """

        url = 'http://127.0.0.1:8000/anuncio'
        data = {
            "imovel_id": 'invalid id',
            "plataforma": "5A",
            "taxa_plataforma": 150.50
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ReservaTests(APITestCase):
    def test_create_reserva_success(self):
        """
        Ensure we can create a new reserva object.
        """
        # creating imovel to use id
        url = 'http://127.0.0.1:8000/imovel'
        data = {
            "max_hospedes": 3,
            "banheiros": 2,
            "pet": True,
            "limpeza": 150.50,
        }
        self.client.post(url, data, format='json')

        # creating anuncio to use id
        url = 'http://127.0.0.1:8000/anuncio'
        data = {
            "imovel_id": Imovel.objects.get().id,
            "plataforma": "5A",
            "taxa_plataforma": 150.50
        }
        self.client.post(url, data, format='json')

        url = 'http://127.0.0.1:8000/reserva'
        data = {
            "anuncio_id": Anuncio.objects.get().id,
            "check_in": "2020-04-21",
            "check_out": "2020-04-23",
            "preco_total": 500.50,
            "comentario": "gostei muito",
            "hospedes": 3
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_create_reserva_fail(self):
        """
        Ensure we can't create a new reserva object using a bad payload.
        """

        url = 'http://127.0.0.1:8000/reserva'
        data = {
            "anuncio_id": 'invalid id',
            "check_in": "2020-04-21",
            "check_out": "2020-04-23",
            "preco_total": 500.50,
            "comentario": "gostei muito",
            "hospedes": 3
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_create_reserva_fail_checkin(self):
        """
        Ensure we can't create a new reserva object using a invalid check_in / check_out.
        """
        # creating imovel to use id
        url = 'http://127.0.0.1:8000/imovel'
        data = {
            "max_hospedes": 3,
            "banheiros": 2,
            "pet": True,
            "limpeza": 150.50,
        }
        self.client.post(url, data, format='json')

        # creating anuncio to use id
        url = 'http://127.0.0.1:8000/anuncio'
        data = {
            "imovel_id": Imovel.objects.get().id,
            "plataforma": "5A",
            "taxa_plataforma": 150.50
        }
        self.client.post(url, data, format='json')

        url = 'http://127.0.0.1:8000/reserva'
        data = {
            "anuncio_id": Anuncio.objects.get().id,
            "check_in": "2020-05-21",
            "check_out": "2020-04-23",
            "preco_total": 500.50,
            "comentario": "gostei muito",
            "hospedes": 3
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)