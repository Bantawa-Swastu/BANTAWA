from django.db import models 

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    feedback = models.TextField()

    def __str__(self):
        return self.name
    
class EventBooked(models.Model):
   name = models.CharField(max_length=255)
   phone = models.CharField(max_length=15)  # Assuming a maximum of 15 characters for a phone number
   category = models.CharField(max_length=100)
   venue = models.CharField(max_length=100)
   date = models.DateField()
   guest = models.IntegerField()
  

   def __str__(self):
        return self.name
   
#for admin fill the venue for users
class AddVenue(models.Model):
    name=models.CharField(max_length=100)
    address=models.TextField(max_length=100)
    capacity=models.TextField()
    images=models.ImageField(upload_to='images/')
    cost=models.IntegerField()



                             