from rest_framework import serializers        #import serializers
from .models import users
from myapp.modules.users_adress.serialisers import users_adress_serialisers
from myapp.modules.users_contact.serialisers import users_contact_serialisers

# JOINTURES
# =======================
# 
#  
class joins_users_serialisers(serializers.ModelSerializer):
    ID_ADRESS = users_adress_serialisers()
    ID_CONTACT = users_contact_serialisers()

    class Meta:
        model=users
        fields="__all__"

# PRINCIPALE
# =======================
# 
#  
class users_serialisers(serializers.ModelSerializer):
    class Meta:
        model=users
        fields="__all__"