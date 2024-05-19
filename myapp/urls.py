from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
 
urlpatterns = [
         path('index/', views.index, name ='index'),
         path('admin/login/', views.login, name = "login"),
         path('admin/login-submit', views.login_submit, name = "login_submit"),
         path('contact_details/', views.contact_details, name='contact_details'),
         path('shop/', views.shop, name = "shop"), 
         path('about/', views.about, name = "about"), 
         path('services/', views.services, name = "services"), 
         path('blog/', views.blog, name = "blog"), 
         path('contact/', views.contact, name = "contact"), 
         path('cart/', views.cart, name ='cart'),
         path('checkout/', views.checkout, name ='checkout'),
         path('contact-form-submit/', views.contact_form_submit, name='contact_form_submit'),
]