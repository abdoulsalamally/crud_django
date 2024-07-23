from .models import users
from .serialisers import users_serialisers
from.serialisers import joins_users_serialisers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

class users_APIView(viewsets.ModelViewSet):
    # queryset = users.objects.all().order_by('NOM')
    # serializer_class = users_serialisers

    queryset = users.objects.all().order_by('NOM')
    serializer_class_read= joins_users_serialisers
    serializer_class_write = users_serialisers
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ["ID_ADRESS","ID_CONTACT"]
    search_fields = ['NOM']

    def get_serializer_class(self):
        if self.request.method in ['GET', 'HEAD']:
            return self.serializer_class_read
        return self.serializer_class_write 