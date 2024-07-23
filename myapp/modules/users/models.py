from django.db import models  #import of the model
from myapp.modules.users_adress.models import users_adress
from myapp.modules.users_contact.models import users_contact

# DECLARATION DES MODELES 
# =======================
# 
#  
class users(models.Model):
    ID_USER = models.AutoField(primary_key=True, db_column='ID_USER')
    ID_ADRESS= models.ForeignKey(users_adress, on_delete=models.CASCADE,null=True,related_name="users",db_column='ID_ADRESS')
    ID_CONTACT= models.ForeignKey(users_contact, on_delete=models.CASCADE,null=True,related_name="users",db_column='ID_CONTACT')
    NOM = models.CharField(max_length=100, null=False, db_column='NOM')
    EMAIL = models.EmailField()
    PHONE = models.CharField(max_length=20, null=False, db_column='PHONE')

    class Meta:
        db_table = 'users'

    def __str__(self):
        return str(self.NOM)