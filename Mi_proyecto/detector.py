import re

INDICATORS = {

    "sql_injection":[
        r"union\s+select",
        r"or\s+1=1",
        r"drop\s+table"
    ],

    "xss":[
        r"<script>",
        r"javascript:"
    ],

    "command_injection":[
        r"whoami",
        r"/etc/passwd",
        r"curl http"
    ]
}


def detect(payload):

    alerts = []

    for attack, patterns in INDICATORS.items():

        for p in patterns:

            if re.search(
                p,
                payload,
                re.IGNORECASE
            ):
                alerts.append(attack)

    return list(set(alerts))