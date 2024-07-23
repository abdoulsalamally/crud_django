from django.db import models  #import of the model

class users_adress(models.Model):
    ID_ADRESS = models.AutoField(primary_key=True, db_column='ID_ADRESS')
    PROVINCE = models.CharField(max_length=100, null=False, db_column='PROVINCE')
    COMMUNE = models.CharField(max_length=20, null=False, db_column='COMMUNE')

    class Meta:
        db_table = 'users_adress'

    def __str__(self):
        return str(self.PROVINCE)