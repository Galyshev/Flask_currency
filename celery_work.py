from celery import Celery
# celery = Celery('celery_work', broker='amqp://guest@localhost:5672//', backend='rpc://' )
celery = Celery('celery_work', broker='amqp://', backend='rpc://')

@celery.task(ignore_result=False)
def add(x, y):
    return x + y

