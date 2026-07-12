from openai import AzureOpenAI
from config import Config

client = AzureOpenAI(
    api_key=Config.AZURE_OPENAI_API_KEY,
    azure_endpoint=Config.AZURE_OPENAI_ENDPOINT,
    api_version="2024-02-01"
)


def analyze_security_event(event_data):

    prompt = f"""
    Actúa como analista SOC nivel 3.

    Analiza este evento:

    {event_data}

    Devuelve:

    - Nivel de riesgo
    - Tipo de amenaza
    - MITRE ATT&CK
    - Recomendaciones
    """

    response = client.chat.completions.create(
        model=Config.DEPLOYMENT_NAME,
        messages=[
            {
                "role": "system",
                "content": "Eres un experto Blue Team."
            },
            {
                "role":"user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content