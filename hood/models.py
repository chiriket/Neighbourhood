from django.db import models
from django.contrib.auth.models import User


class Neighbourhood(models.Model):
    name  = models.CharField(max_length=30)  
    location = models.CharField(max_length =10)
    occupants = models.ForeignKey(User, null = True,related_name='business')
    admin = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    
    def save_neighbourhood(self):
        self.save()

    def delete_neigbourhood(self):
        self.delete()

    # def update_neighbour(self, update):
    #     self.photo_location = update
    #     self.save()

    @classmethod
    def find_neighbourhood_id(cls, id):
        neighbourhood = Neighbourhood.objects.get(pk=id)
        return neighbourhood

class User(models.Model):
    photo = models.ImageField(upload_to = 'images/',blank=True)
    Bio = models.TextField(max_length = 50,null = True)
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)

    def __str__(self):
       return self.first_name

    def save_user(self):
        self.save()

    def delete_user(self):
        self.delete()

    @classmethod
    def get_users(cls):
        profiles = cls.objects.all()
        return profiles
    
   
class Business (models.Model):
    name = models.CharField(max_length=50,blank=True)
    image = models.ImageField(upload_to = 'images/')
    user = models.ForeignKey(User, null = True,related_name='user')
    neighbourhood = models.ForeignKey(Neighbourhood, null = True,related_name='business')
    email = models.EmailField()

    @classmethod
    def search_by_neighbourhood(cls,search_term):
        business = cls.objects.filter(neighbourhood__icontains=search_term)
        return business