from fastapi import FastAPI, APIRouter
from models import Event
import logging


router = APIRouter()
app = FastAPI()


def get_logger():
    logger = logging.getLogger('tile38')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
    if not logger.hasHandlers():
        file_handler = logging.FileHandler('logs.log')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger

@app.post("/endpoint", status_code=200)
async def webhook(event: Event) -> dict:
    get_logger().info(event)
    return ''#event

