from django.core import serializers
from .models import cutoff


class CutoffSerializers(serializers.Modelserializers):
    class Meta:
        model = cutoff
        fields="__all__"
