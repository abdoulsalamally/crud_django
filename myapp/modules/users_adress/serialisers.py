from rest_framework import serializers        #import serializers
from .models import users_adress


class users_adress_serialisers(serializers.ModelSerializer):
    class Meta:
        model=users_adress
        fields="__all__"