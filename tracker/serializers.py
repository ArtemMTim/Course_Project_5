from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .validators import HabitValidator
from .models import Habits
from users.serializers import UserSerializer


class HabitsSerializer(ModelSerializer):
    """Сериализатор привычки."""
    creater = UserSerializer(read_only=True)

    class Meta:
        model = Habits
        fields = '__all__'
        validators = [HabitValidator(field="__all__")]
