from rest_framework import serializers

class action_time:
    def __init__(self, field):
        self.field = field
    def __call__(self, value):
        time = dict(value).get(self.field)
        if int(time) > 120:
            raise serializers.ValidationError("Время выполнения привычки не может превышать 120 секунд.")

class action_periodicity:
    def __init__(self, field):
        self.field = field
    def __call__(self, value):
        periodicity = dict(value).get(self.field)
        if int(periodicity) > 7:
            raise serializers.ValidationError("Периодичность выполнения привычки не может быть реже раза в неделю.")