from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'libros', views.LibroViewSet)

urlpatterns = [
    path('libros/<nombre>/', views.LibroViewSet.as_view({'get': 'retrieve'}), name='libro-detail'),
    #path('', include(router.urls)),
]