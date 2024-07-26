# Create your models here.
import uuid
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from base.models import BaseModel
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from account.models import Farm
#Relation entre livestock et farm coz un livestock belongs to a farm 

class LiveStock(BaseModel):

    ANIMAL_TYPES = [
        ('COW','Cow'),
        ('Sheep', 'Sheep'),
        ('Pig', 'Pig'),
    ]

    ACQUISITION_METHODS = [
        ('Born', 'Born'),
        ('Purchased', 'Purchased'),
    ]

    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Sold', 'Sold'),
        ('Deceased', 'Deceased'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    objects = Farm() 
    farm_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    animal_type = models.CharField(_("animal type"), max_length=10, choices=ANIMAL_TYPES)
    breed = models.CharField(_("breed"), max_length=10, blank=True)
    name = models.CharField(_("name"), max_length=100, blank=True, null=True)
    tag_number = models.CharField(_("tag number"), max_length=50, blank=True)
    date_of_birth = models.DateField(_("date of birth"), null=True, blank=True)
    gender = models.CharField(_("gender"), max_length=10, blank=True)
    acquisistion_date = models.DateField(_("acquisition date"), null=True, blank=True)
    acquisistion_method = models.CharField(_("acquisition method"),max_length=10, choices=ACQUISITION_METHODS)
    status = models.CharField(_("status"),max_length=10, choices=STATUS_CHOICES)
    current_weight = models.FloatField(_("weight"), max_length=10, blank=True)
    current_age = models.IntegerField(_("age"), blank=True)
    photo = models.ImageField(_("profile picture"), upload_to="static/profile_pictures/", blank=True, null=True)

    def __str__(self):
        return f"{self.animal_type} - {self.tag_number}"
    
    def __str__(self):
        return self.name
    
