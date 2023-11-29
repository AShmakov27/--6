# /app/rabbitmq.py
import json
import traceback
from asyncio import AbstractEventLoop
from aio_pika.abc import AbstractRobustConnection
from aio_pika import connect_robust, IncomingMessage
from settings import settings
from services.attendance_service import AttendanceService

async def process_created_lesson(msg: IncomingMessage):
    try:
        data = json.loads(msg.body.decode())
        AttendanceService().create_lesson(id=data['lesson_id'],date=data['date'],subject=data['subject'])
    except:
        traceback.print_exc()
        await msg.ack()

async def process_created_student(msg: IncomingMessage):
    try:
        data = json.loads(msg.body.decode())
        AttendanceService().create_student(id=data['student_id'], FIO=data['FIO'])
    except:
        traceback.print_exc()
        await msg.ack()
    pass

async def consume(loop: AbstractEventLoop) -> AbstractRobustConnection: 
    connection = await connect_robust(settings.amqp_url, loop=loop) 
    channel = await connection.channel() 

    lesson_created_queue = await channel.declare_queue('lesson_created_queue', durable=True)
    student_created_queue = await channel.declare_queue('student_created_queue', durable=True)
    
    await lesson_created_queue.consume(process_created_lesson)
    await student_created_queue.consume(process_created_student)
    print ('Started RabbitMQ consuming...') 

    return connection
