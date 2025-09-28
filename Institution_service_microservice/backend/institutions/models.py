import uuid
from django.db import models


class Institucion(models.Model):
    TIPO_CHOICES = [
        ("colegio", "Colegio"),
        ("universidad", "Universidad"),
        ("instituto", "Instituto"),
        ("centro_formacion", "Centro de Formación"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=255, unique=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    ruc = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    sitio_web = models.URLField(blank=True, null=True)
    logo_url = models.URLField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Representante(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    institucion = models.ForeignKey(
        Institucion, on_delete=models.CASCADE, related_name="representantes"
    )
    usuario_id = models.UUIDField()  # referencia lógica a auth_service
    cargo = models.CharField(max_length=100)
    es_principal = models.BooleanField(default=False)
    fecha_asignacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cargo} - {self.institucion.nombre}"


class CarreraOfertada(models.Model):
    MODALIDAD_CHOICES = [
        ("presencial", "Presencial"),
        ("virtual", "Virtual"),
        ("hibrida", "Híbrida"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    institucion = models.ForeignKey(
        Institucion, on_delete=models.CASCADE, related_name="carreras"
    )
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    duracion_meses = models.IntegerField(blank=True, null=True)
    modalidad = models.CharField(max_length=20, choices=MODALIDAD_CHOICES)
    costo_anual = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    requisitos = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.institucion.nombre}"


class Sede(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    institucion = models.ForeignKey(
        Institucion, on_delete=models.CASCADE, related_name="sedes"
    )
    nombre = models.CharField(max_length=255)
    direccion = models.TextField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    es_principal = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} - {self.institucion.nombre}"
