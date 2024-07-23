from .models import users_contact
from .serialisers import users_contact_serialisers
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

class users_contact_APIView(viewsets.ModelViewSet):
    queryset = users_contact.objects.all().order_by('MOBILE_PHONE')
    serializer_class = users_contact_serialisers
