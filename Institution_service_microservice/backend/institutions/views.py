from rest_framework import viewsets
from .models import Institucion, Representante, CarreraOfertada, Sede
from .serializers import (
    InstitucionSerializer,
    RepresentanteSerializer,
    CarreraOfertadaSerializer,
    SedeSerializer,
)


class InstitucionViewSet(viewsets.ModelViewSet):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer


class RepresentanteViewSet(viewsets.ModelViewSet):
    queryset = Representante.objects.all()
    serializer_class = RepresentanteSerializer


class CarreraOfertadaViewSet(viewsets.ModelViewSet):
    queryset = CarreraOfertada.objects.all()
    serializer_class = CarreraOfertadaSerializer


class SedeViewSet(viewsets.ModelViewSet):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer
