from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .serializers import UserSerializer, UserDetailSerializer

User = get_user_model()


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"
    permission_classes = [IsAdminUser]

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        if self.request.user.is_superuser:
            return self.queryset
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False, permission_classes=[IsAuthenticated])
    def me(self, request):
        serializer = UserDetailSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)
