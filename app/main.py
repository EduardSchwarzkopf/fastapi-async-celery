import uvicorn

from fastapi import FastAPI

from app.tasks import example_task

app = FastAPI(title="Example")


@app.get("/example")
async def example():
    example_task.delay()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0")
