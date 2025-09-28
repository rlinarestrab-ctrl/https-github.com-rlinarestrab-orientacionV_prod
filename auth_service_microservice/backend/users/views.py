from django.db.models import Q
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Usuario
from .serializers import UsuarioSerializer
from .permissions import IsAdmin, IsSelfOrAdmin

class UserViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all().order_by("-fecha_registro")
    serializer_class = UsuarioSerializer

    def get_permissions(self):
        if self.action in ["list", "create", "destroy"]:
            return [IsAdmin()]
        if self.action in ["retrieve", "update", "partial_update"]:
            return [IsSelfOrAdmin()]
        return super().get_permissions()

    def list(self, request, *args, **kwargs):
        q = request.query_params.get("q")
        qs = self.get_queryset()
        if q:
            qs = qs.filter(
                Q(email__icontains=q) |
                Q(nombre__icontains=q) |
                Q(apellido__icontains=q)
            )
        page = self.paginate_queryset(qs)
        if page is not None:
            ser = self.get_serializer(page, many=True)
            return self.get_paginated_response(ser.data)
        ser = self.get_serializer(qs, many=True)
        return Response(ser.data)
