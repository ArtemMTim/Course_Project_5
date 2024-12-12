from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from .models import Habits
from .serializers import HabitsSerializer


class HabitsListApiView(ListAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer

    def get_queryset(self):
        return Habits.objects.filter(is_public=True)


class HabitsCreateApiView(CreateAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.creater = self.request.user
        habit.save()


class HabitsRetrieveApiView(ListAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer


class HabitsUpdateApiView(UpdateAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer


class HabitsDestroyApiView(DestroyAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
