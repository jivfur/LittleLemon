from django.shortcuts import render

from rest_framework.generics import ListCreateView,RetrieveUpdateAPIView,DestroyAPIView
from rest_framework.response import Response

from .models import Menu
from .serializers import MenuSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(ListCreateView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(RetrieveUpdateAPIView,DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer