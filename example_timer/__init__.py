import datetime
import azure.functions as func


def main(timer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().isoformat()
    print(f"Timer trigger function executed at {utc_timestamp}")