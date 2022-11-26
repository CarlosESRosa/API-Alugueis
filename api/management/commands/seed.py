import requests
from django.core.management.base import BaseCommand
from ...models import Imovel, Anuncio, Reserva 

def seed_imovel():
    imoveis_json = [
        {"max_hospedes": 1, "banheiros": 1, "pet": True, "limpeza": 150.50},
        {"max_hospedes": 2, "banheiros": 2, "pet": True, "limpeza": 150.50},
        {"max_hospedes": 3, "banheiros": 2, "pet": False, "limpeza": 120.50},
        {"max_hospedes": 4, "banheiros": 3, "pet": True, "limpeza": 100.50},
        {"max_hospedes": 5, "banheiros": 4, "pet": False, "limpeza": 250.50},
    ]
    for imovel in imoveis_json:
        imovel = Imovel(
            max_hospedes=imovel["max_hospedes"],
            banheiros=imovel["banheiros"],
            pet=imovel["pet"],
            limpeza=imovel["limpeza"],
        )
        imovel.save()



def seed_anuncio():
    example_imovel = Imovel.objects.filter()[0]
    anuncios_json = [
        {"imovel_id": example_imovel, "plataforma": "5A", "taxa_plataforma": 150.50},
        {"imovel_id": example_imovel, "plataforma": "AirBnB", "taxa_plataforma": 250.50},
        {"imovel_id": example_imovel, "plataforma": "5A", "taxa_plataforma": 200},
    ]
    for anuncio in anuncios_json:
        anuncio = Anuncio(
            imovel_id=anuncio["imovel_id"],
            plataforma=anuncio["plataforma"],
            taxa_plataforma=anuncio["taxa_plataforma"],
        )
        anuncio.save()

def seed_reserva():
    example_anuncio = Anuncio.objects.filter()[0]
    reservas_json = [
        {"anuncio_id": example_anuncio, "check_in": "2023-04-21", "check_out": "2023-04-23", "preco_total": 100.50, "comentario": "gostei muito", "hospedes": 3 },
        {"anuncio_id": example_anuncio, "check_in": "2023-05-21", "check_out": "2023-05-23", "preco_total": 200.50, "comentario": "gostei muito", "hospedes": 4 },
        {"anuncio_id": example_anuncio, "check_in": "2023-04-25", "check_out": "2023-04-26", "preco_total": 300.50, "comentario": "gostei muito", "hospedes": 5 },
        {"anuncio_id": example_anuncio, "check_in": "2023-04-22", "check_out": "2023-04-23", "preco_total": 400.50, "comentario": "gostei muito", "hospedes": 6 },
        {"anuncio_id": example_anuncio, "check_in": "2023-04-20", "check_out": "2023-04-23", "preco_total": 500.50, "comentario": "gostei muito", "hospedes": 7 },
        {"anuncio_id": example_anuncio, "check_in": "2023-04-19", "check_out": "2023-04-23", "preco_total": 600.50, "comentario": "gostei muito", "hospedes": 8 },
        {"anuncio_id": example_anuncio, "check_in": "2023-04-10", "check_out": "2023-04-23", "preco_total": 700.50, "comentario": "gostei muito", "hospedes": 10 },
        {"anuncio_id": example_anuncio, "check_in": "2023-04-12", "check_out": "2023-04-23", "preco_total": 800.50, "comentario": "gostei muito", "hospedes": 12 },
    ]
    for reserva in reservas_json:
        reserva = Reserva(
            anuncio_id=reserva["anuncio_id"],
            check_in=reserva["check_in"],
            check_out=reserva["check_out"],
            preco_total=reserva["preco_total"],
            comentario=reserva["comentario"],
            hospedes=reserva["hospedes"],
        )
        reserva.save()


def clear_data():
  Imovel.objects.all().delete()
  Anuncio.objects.all().delete()
  Reserva.objects.all().delete()


class Command(BaseCommand):
  def handle(self, *args, **options):
    clear_data()
    seed_imovel()
    seed_anuncio()
    seed_reserva()
    print("completed")