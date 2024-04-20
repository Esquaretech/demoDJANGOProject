from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
 
urlpatterns = [
         path('index/', views.index, name ='index'),
         path('shop/', views.shop, name = "shop"), 
         path('about/', views.about, name = "about"), 
         path('services/', views.services, name = "services"), 
         path('blog/', views.blog, name = "blog"), 
         path('contact/', views.contact, name = "contact"), 
]