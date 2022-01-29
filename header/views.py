from rest_framework import viewsets

from .serializers import *
from .models import *


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.filter(parent__isnull=True)
    serializer_class = MenuSerializer

class LogoViewSet(viewsets.ModelViewSet):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer


    # def get_permissions(self):
    #     # Your logic should be all here
    #     if self.request.method == 'GET':
    #         self.permission_classes = [IsAuthenticated, ]
    #     else:
    #         self.permission_classes = [IsAdminUser, ]
    #
    #     return super(MenuList, self).get_permissions()


