from django.contrib import admin
from .models import Feedback
from .models import EventBooked
from .models import AddVenue

# Register your models here.
admin.site.register(Feedback)

admin.site.register(EventBooked)

admin.site.register(AddVenue)




