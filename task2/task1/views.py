from rest_framework import permissions, viewsets

from .models import Person
from .serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows persons to be viewed.
    """
    # add code here
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    http_method_names = ['get']
