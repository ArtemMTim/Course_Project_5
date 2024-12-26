from datetime import timedelta, datetime
from tracker.models import Habits
from celery import shared_task


@shared_task
def habit_to_do_reminder():
    """Проверяет необходимост выполнения привычки. Возвращает сообщение-напоминание и id Телеграмма пользователя."""
    result = []
    today = datetime.now().date()
    habits = Habits.objects.filter(is_pleasant=False)
    for habit in habits:
        #проверяем необходимость выполнения привычки сегодня
        if (today - habit.last_action_date).days == habit.periodicity:
            #проверяем пришло ли время выполнения привычки
            if datetime.combine(datetime.now(), habit.time_to_do) - datetime.now() <= timedelta(minutes=10):
                message =  f"Напоминаем вам, что вам следует {habit.action_to_do} в {habit.place_to_do} в {habit.time_to_do}."
                tg_id = habit.creater.tg_id
                result.append((message, tg_id))
                #обновляем дату последнего действия привычки
                habit.last_action_date = today
                habit.save()
    #return result
    print(result)