from django.shortcuts import render
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from django.http import HttpResponse

from .models import Person
from .serializers import PersonSerializer

### Views

# View for listing and creating users.
class PersonListCreateView(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


# View for retrieving, updating, and deleting a given user
class PersonRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


# To handle wrong endpoints or inputs
def endpoint_error_handler(request, exception):
	return HttpResponse(f"<b>You entered a wrong input or endpiont</b> <br> <i>to check valid endpoints click on: </i> <a href='/swagger/'> endpoints</a> \
                      <br> <i>to check list of persons click on: </i> <a href='/api/'> persons</a> ")