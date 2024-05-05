from app.worker import celery


@celery.task
async def example_task() -> str:
    msg = "Hello World"
    print(msg)
    return msg
