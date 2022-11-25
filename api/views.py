from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Imovel
from .serializers import ImovelSerializer

class ImovelListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Imovel items
        '''
        imoveis = Imovel.objects.filter()
        serializer = ImovelSerializer(imoveis, many=True)
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