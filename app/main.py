from fastapi import FastAPI, APIRouter
from models import Event
from loggers import get_inside_logger, get_misc_events_logger


router = APIRouter()
app = FastAPI()


@app.post("/endpoint", status_code=200)
async def webhook(event: Event) -> dict:
    if event.detect == 'inside':
        get_inside_logger().info(event)
    else:
        get_misc_events_logger().info(event)
    return event

