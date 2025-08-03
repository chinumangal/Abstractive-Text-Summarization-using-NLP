from flask import Flask
from app.routes import summarize_blueprint, home_blueprint
from flask_cors import CORS

app = Flask(__name__)

CORS(app, supports_credentials=True, headers=['Content-Type', 'Authorization'], origin='http://localhost:5173')

app.register_blueprint(home_blueprint, url_prefix="/")
app.register_blueprint(summarize_blueprint, url_prefix="/summarize")

if __name__ == "__main__":
    app.run(port=8000, debug=True)
