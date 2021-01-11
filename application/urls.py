from django.urls import path, include
from rest_framework import routers

from application import views

router = routers.DefaultRouter()

# router.register('org',views.OrganizationCRUD)
router.register('emp', views.EmployeeCRUD)
router.register('register', views.RegisterAPI)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.login),
]
