import os

class Config:

    AZURE_OPENAI_ENDPOINT = os.getenv(
        "AZURE_OPENAI_ENDPOINT"
    )

    AZURE_OPENAI_API_KEY = os.getenv(
        "AZURE_OPENAI_API_KEY"
    )

    DEPLOYMENT_NAME = os.getenv(
        "AZURE_OPENAI_DEPLOYMENT"
    )

    SECRET_KEY = os.getenv(
        "SECRET_KEY"
    )