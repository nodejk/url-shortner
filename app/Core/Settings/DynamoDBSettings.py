import os
import pydantic


class DynamoDBSettings(pydantic.BaseSettings):
    table_name: str
    access_key_id: str = os.environ["AWS_ACCESS_KEY_ID"]
    secret_access_key: str = os.environ["AWS_SECRET_ACCESS_KEY"]
    region_name: str = os.environ["REGION"]
    service_name: str = "dynamodb"
