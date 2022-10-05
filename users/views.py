from rest_framework.generics import CreateAPIView

from users.models import User
from users.serializers import RegisterSerializer

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer