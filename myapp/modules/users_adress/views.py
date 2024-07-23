from .models import users_adress
from .serialisers import users_adress_serialisers
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

class users_adress_APIView(viewsets.ModelViewSet):
    queryset = users_adress.objects.all().order_by('PROVINCE')
    serializer_class = users_adress_serialisers
