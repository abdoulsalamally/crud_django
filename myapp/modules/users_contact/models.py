from django.db import models  #import of the model
# DECLARATION DES MODELES 
# =======================
# 
#  
class users_contact(models.Model):
    ID_CONTACT = models.AutoField(primary_key=True, db_column='ID_CONTACT')
    MOBILE_PHONE = models.CharField(max_length=100, null=False, db_column='MOBILE_PHONE')
    HOME_PHONE = models.CharField(max_length=100, null=False, db_column='HOME_PHONE')

    class Meta:
        db_table = 'users_contact'

    def __str__(self):
        return str(self.MOBILE_PHONE)