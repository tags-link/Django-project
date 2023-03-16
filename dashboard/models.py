from django.db import models
from django.contrib.auth.models import User

# Create your models here.

gender = (
    ('MALE','MALE'),('FEMALE','FEMALE')
)
marital_status = (
    ('SINGLE','SINGLE'),('MARRIED','MARRIED')
)

state_of_origin = (
    ('Abia','Abia'),('Adamawa','Adamawa'),('Akwa Ibom','Akwa Ibom'),
)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=20,default='')
    DoB =models.DateField()
    gendre = models.CharField(max_length=7,choices=gender)
    state_of_origin = models.CharField(max_length=10,choices=state_of_origin,default='')
    lga_of_origin = models.CharField(max_length=100,default='')
    scheme_name = models.CharField(max_length=10,blank=True,null=True,default='')
    phone_number = models.IntegerField()
    year_of_application = models.CharField(max_length=4,default='')
    profile_pics = models.ImageField(upload_to='profile_pics',default='')
    address = models.TextField(max_length=200,default='')
    marital_status = models.CharField(max_length=15,choices=marital_status,default='')
    
    def __str__(self) -> str:
        return f'{self.user}'