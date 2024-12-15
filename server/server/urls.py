from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('powercalculation/', views.power, name="powercalculation"),
    path('', views.power, name="powerroot"),
]
