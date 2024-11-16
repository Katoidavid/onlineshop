"""
URL configuration for OnlineShop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# customers/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='home'),          # Home page accessible at /customers/
    path('about/', views.about, name='about_us'),      # About Us page accessible at /customers/about/
    path('features/', views.features, name='features'),# Features page at /customers/features/
    path('pricing/', views.pricing, name='pricing'),   # Pricing page at /customers/pricing/
    path('contact/', views.contact, name='contact'),   # Contact Us page at /customers/contact/
    path('contact1/', views.contact1, name='contact1'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
