import asyncio
from fastapi import FastAPI
from endpoints.lesson_router import lesson_router
import rabbitmq
from settings import settings

app = FastAPI(title='Attendance Service')

@app.on_event('startup')
def startup():
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(rabbitmq.consume(loop))


app.include_router(lesson_router, prefix='/api')