from celery import Celery
celery = Celery('celery_work', broker='amqp://guest@localhost:5672//')


# перед запуском воркера во втором терминале запустить "celery -A celery_work beat -s ./utils/celerybeat-schedule.db"
@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(15.0, print_word.s('periodic text'), name='name_work')

@celery.task()
def print_word(string):
    print(string)
    return f"Input word: {string}"

