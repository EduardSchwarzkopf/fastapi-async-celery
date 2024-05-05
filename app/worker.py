from celery import Celery
from inspect import isawaitable
import asyncio


class AsyncCelery(Celery):
    # Credits: Cyril N.
    # https://stackoverflow.com/a/69585025/11699898

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.patch_task()

        if "app" in kwargs:
            self.init_app(kwargs["app"])

    def patch_task(self):
        TaskBase = self.Task

        class ContextTask(TaskBase):
            abstract = True

            async def _run(self, *args, **kwargs):
                result = TaskBase.__call__(self, *args, **kwargs)
                if isawaitable(result):
                    await result

            def __call__(self, *args, **kwargs):
                asyncio.run(self._run(*args, **kwargs))

        self.Task = ContextTask

    def init_app(self, app):
        self.app = app

        conf = {}
        for key in app.config.keys():
            if key[0:7] == "CELERY_":
                conf[key[7:].lower()] = app.config[key]

        if (
            "broker_transport_options" not in conf
            and conf.get("broker_url", "")[0:4] == "sqs:"
        ):
            conf["broker_transport_options"] = {"region": "eu-west-1"}

        self.config_from_object(conf)


celery = AsyncCelery(
    "worker",
    broker="redis://127.0.0.1:6379/0",
    include=["app.tasks"],
)
