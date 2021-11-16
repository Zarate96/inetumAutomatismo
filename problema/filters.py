import django_filters

from .models import *

class GestionFilter(django_filters.FilterSet):
    class Meta:
        model = Gestion
        fields = "estatus",