from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Imovel, Anuncio, Reserva
from .serializers import ImovelSerializer, AnuncioSerializer, ReservaSerializer

class ImovelListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Imovel items
        '''
        imoveis = Imovel.objects.filter()
        serializer_context = {
            'request': request,
        }
        serializer = ImovelSerializer(imoveis, context=serializer_context, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Imovel with given Imovel data
        '''
        data = {
            'max_hospedes': request.data.get('max_hospedes'),
            'banheiros': request.data.get('banheiros'),
            'pet': request.data.get('pet'),
            'limpeza': request.data.get('limpeza'),
        }
        serializer = ImovelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImovelDetailApiView(APIView):

    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self, imovel_id):
        '''
        Helper method to get the object with given imovel_id
        '''
        try:
            return Imovel.objects.get(id=imovel_id)
        except Imovel.DoesNotExist:
            return None

    # 3. List One
    def get(self, request, imovel_id, *args, **kwargs):
        '''
        Retrieves the imovel with given imovel_id
        '''
        imovel_instance = self.get_object(imovel_id)
        if not imovel_instance:
            return Response(
                {"res": "Imovel with imovel id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ImovelSerializer(imovel_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, imovel_id, *args, **kwargs):
        '''
        Updates the imovel item with given imovel_id if exists
        '''
        imovel_instance = self.get_object(imovel_id)
        if not imovel_instance:
            return Response(
                {"res": "Imovel with imovel id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'max_hospedes': request.data.get('max_hospedes'),
            'banheiros': request.data.get('banheiros'),
            'pet': request.data.get('pet'),
            'limpeza': request.data.get('limpeza'),
        }
        serializer = ImovelSerializer(instance = imovel_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, imovel_id, *args, **kwargs):
        '''
        Deletes the imovel item with given imovel_id if exists
        '''
        imovel_instance = self.get_object(imovel_id)
        if not imovel_instance:
            return Response(
                {"res": "Imovel with imovel id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        imovel_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class AnuncioListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Anuncio items
        '''
        anuncios = Anuncio.objects.filter()

        serializer = AnuncioSerializer(anuncios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Imovel with given Imovel data
        '''
        data = {
            'imovel_id': request.data.get('imovel_id'),
            'plataforma': request.data.get('plataforma'),
            'taxa_plataforma': request.data.get('taxa_plataforma'),
        }
        serializer = AnuncioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnuncioDetailApiView(APIView):

    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self, anuncio_id):
        '''
        Helper method to get the object with given anuncio_id
        '''
        try:
            return Anuncio.objects.get(id=anuncio_id)
        except Anuncio.DoesNotExist:
            return None

    # 3. List One
    def get(self, request, anuncio_id, *args, **kwargs):
        '''
        Retrieves the anuncio with given anuncio_id
        '''
        anuncio_instance = self.get_object(anuncio_id)
        if not anuncio_instance:
            return Response(
                {"res": "Anuncio with anuncio id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = AnuncioSerializer(anuncio_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, anuncio_id, *args, **kwargs):
        '''
        Updates the anuncio item with given anuncio_id if exists
        '''
        anuncio_instance = self.get_object(anuncio_id)
        if not anuncio_instance:
            return Response(
                {"res": "Anuncio with anuncio id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'imovel_id': request.data.get('imovel_id'),
            'plataforma': request.data.get('plataforma'),
            'taxa_plataforma': request.data.get('taxa_plataforma')
        }
        serializer = AnuncioSerializer(instance = anuncio_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReservaListApiView(APIView):

    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Reserva items
        '''
        reservas = Reserva.objects.filter()

        serializer = ReservaSerializer(reservas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Reserva with given Reserva data
        '''
        data = {
            'anuncio_id': request.data.get('anuncio_id'),
            'check_in': request.data.get('check_in'),
            'check_out': request.data.get('check_out'),
            'preco_total': request.data.get('preco_total'),
            'comentario': request.data.get('comentario'),
            'hospedes': request.data.get('hospedes'),
        }

        serializer = ReservaSerializer(data=data)
        if serializer.is_valid():
            if data['check_in'].replace("-", "") > data['check_out'].replace("-", ""):
                return Response({ "detail": 'invalid Check_in or Check_out'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReservaDetailApiView(APIView):

    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self, reserva_id):
        '''
        Helper method to get the object with given reserva_id
        '''
        try:
            return Reserva.objects.get(id=reserva_id)
        except Reserva.DoesNotExist:
            return None

    # 3. List One
    def get(self, request, reserva_id, *args, **kwargs):
        '''
        Retrieves the reserva with given reserva_id
        '''
        reserva_instance = self.get_object(reserva_id)
        if not reserva_instance:
            return Response(
                {"res": "Reserva with reserva id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ReservaSerializer(reserva_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 5. Delete
    def delete(self, request, reserva_id, *args, **kwargs):
        '''
        Deletes the reserva item with given reserva_id if exists
        '''
        reserva_instance = self.get_object(reserva_id)
        if not reserva_instance:
            return Response(
                {"res": "Reserva with reserva id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        reserva_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )