from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Habits


class HabitsSerializer(ModelSerializer):
    class Meta:
        model = Habits
        fields = "__all__"
