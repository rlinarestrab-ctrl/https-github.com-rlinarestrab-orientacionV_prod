from rest_framework import serializers
from django.contrib.auth import authenticate
from django.utils import timezone
from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Usuario
        fields = [
            "id", "email", "password", "nombre", "apellido",
            "fecha_nacimiento", "telefono", "rol",
            "fecha_registro", "ultimo_login", "activo"
        ]
        read_only_fields = ["fecha_registro", "ultimo_login", "id"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = Usuario(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(request=self.context.get("request"), email=email, password=password)
        if not user:
            raise serializers.ValidationError("Credenciales inválidas")

        user.ultimo_login = timezone.now()
        user.save(update_fields=["ultimo_login"])

        attrs["user"] = user
        return attrs
