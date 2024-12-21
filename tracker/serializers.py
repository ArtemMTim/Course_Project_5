from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .validators import action_time, action_periodicity
from .models import Habits
from users.serializers import UserSerializer


class HabitsSerializer(ModelSerializer):
    """Сериализатор привычки."""
    creater = UserSerializer(read_only=True)

    class Meta:
        model = Habits
        fields = (
        "creater",
        "place_to_do",
        "time_to_do",
        "action_to_do",
        "is_pleasant",
        "related_habit",
        "periodicity",
        "reward",
        "duration",
        "is_public",
    )
        validators = (action_time(field="duration"), action_periodicity(field="periodicity"))
