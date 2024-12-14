from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)

from users.permissions import IsCreater

from .models import Habits
from .serializers import HabitsSerializer


class HabitsPublicListApiView(ListAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer

    def get_queryset(self):
        return Habits.objects.filter(is_public=True)


class HabitsUsersListApiView(ListAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer

    def get_queryset(self):
        return Habits.objects.filter(creater=self.request.user)


class HabitsCreateApiView(CreateAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.creater = self.request.user
        habit.save()


class HabitsRetrieveApiView(RetrieveAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer

    def get_permissions(self):
        self.permission_classes = (IsCreater,)
        return super().get_permissions()


class HabitsUpdateApiView(UpdateAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer

    def get_permissions(self):
        self.permission_classes = (IsCreater,)
        return super().get_permissions()


class HabitsDestroyApiView(DestroyAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer

    def get_permissions(self):
        self.permission_classes = (IsCreater,)
        return super().get_permissions()
