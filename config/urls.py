from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('about', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
