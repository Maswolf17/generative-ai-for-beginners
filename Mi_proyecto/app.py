from flask import Flask
from routes.security import security_bp

app = Flask(__name__)

app.register_blueprint(
    security_bp,
    url_prefix="/api/v1"
)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )