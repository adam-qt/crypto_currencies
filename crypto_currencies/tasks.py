from celery import app
from .services import download_data_from_api, parse_data_to_db


@app.shared_task
def update_db():
    parse_data_to_db(download_data_from_api())