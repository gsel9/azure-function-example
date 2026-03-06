import datetime
import logging

import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    now = datetime.datetime.utcnow().isoformat()
    logging.info(f"Timer ran at {now}")

    # Your script logic here
    print("Hello from scheduled Azure function")
