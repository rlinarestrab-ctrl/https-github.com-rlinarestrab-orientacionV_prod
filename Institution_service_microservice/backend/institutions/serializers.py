from rest_framework import serializers
from .models import Institucion, Representante, CarreraOfertada, Sede


class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields = "__all__"


class CarreraOfertadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarreraOfertada
        fields = "__all__"


class RepresentanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Representante
        fields = "__all__"


class InstitucionSerializer(serializers.ModelSerializer):
    sedes = SedeSerializer(many=True, read_only=True)
    carreras = CarreraOfertadaSerializer(many=True, read_only=True)
    representantes = RepresentanteSerializer(many=True, read_only=True)

    class Meta:
        model = Institucion
        fields = "__all__"
