from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home, name="home"),

    #auth
    path('signin/', views.signin, name="signin"),

    path('signup/', views.signup, name="signup"),
    
    path('', views.signout, name="signout"),

    #admin urls
    path('dashboard/',views.dashboard1,name='dashboard'),

    path('addvenue/',views.addvenue,name='venue'),

    path('admindashboard/', views.admindash, name='admindashboard'),

    path('viewfeedback/',views.viewfeedback,name='viewfeedback'),

    path('newbooked/',views.newbooked,name='newbooked'),
    
    #URL for accept an event
    path('accept/<int:event_id>/', views.accept_event, name='accept_event'),

    # URL for deleting an event
    path('delete/<int:event_id>/', views.delete_event, name='delete_event'),


    #user urls
    path('userdashboard/',views.userdashboard,name='dashboard'),

    path('event/',views.event,name='booking_event'),
    
    path('feedback/',views.feedback,name='feedback'),

    path('vwvenue/',views.vwvenue,name='viewvenue'),
   
   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)