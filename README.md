# AsyncCelery Integration for FastAPI Applications

This repository demonstrates how to integrate asynchronous task processing into FastAPI applications using a custom `AsyncCelery` class. This approach allows for seamless execution of asynchronous tasks within a Celery worker, aligning with the asynchronous requirements of FastAPI and `AsyncSession`.

## Features

- **Custom AsyncCelery Class**: Extends Celery's functionality to support asynchronous tasks, leveraging Python's `asyncio` library for asynchronous execution.
- **Integration with FastAPI**: Demonstrates how to initialize the Celery worker with the custom class and define asynchronous tasks callable from FastAPI endpoints.
- **Efficient AsyncSession Management**: Addresses the challenges of integrating `AsyncSession` with Celery, enhancing performance and scalability.

## Getting Started

### Prerequisites

- Python 3.8+
- Docker
- FastAPI
- Celery
- Redis (for Celery broker)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/async-celery-fastapi.git
cd async-celery-fastapi
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run Redis:

```bash
docker run --rm --name celery-redis -p 6379:6379 redis:latest
```

4. Run the FastAPI application:

```bash
uvicorn main:app --reload
```

5. Start the Celery worker:

```bash
celery -app=app.worker -- worker --loglevel=debug
```

6. Visit `http://127.0.0.1:8000/example` to run the process

### Debug

I've included the `launch.json` so you can use the VSCode Debugger to start debugging.