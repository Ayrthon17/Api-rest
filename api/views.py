from rest_framework import viewsets
from .serializer import LibroSerializer
from .models import Libro
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

# Create your views here.
class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    
    def retrieve(self, request, nombre=None):
        try:
            libro = self.queryset.get(nombre=nombre)
            serializer = self.get_serializer(libro)
            return Response(serializer.data)
        except Libro.DoesNotExist:
            raise NotFound(detail="El libro no ha sido encontrado")

    def create(self, request):
        # Verificar si ya existe un libro con el mismo nombre
        nombre_libro = request.data.get('nombre')
        if Libro.objects.filter(nombre=nombre_libro).exists():
            return Response({"detail": f"El libro con nombre '{nombre_libro}' ya existe"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, nombre=None):  # Change pk to nombre
        try:
            libro = self.queryset.get(nombre=nombre)
            libro.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Libro.DoesNotExist:
            return Response({"detail": f"Libro con nombre '{nombre}' no encontrado"}, status=status.HTTP_404_NOT_FOUND)

# Create your views here.
