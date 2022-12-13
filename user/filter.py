import django_filters
from upload.models import *

class FilterClass(django_filters.FilterSet):
    class Meta:
        model=Book
        fields=['course','university']