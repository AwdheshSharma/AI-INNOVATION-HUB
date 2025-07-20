from flask import Flask
from config import Config
from blueprints import register_blueprints

app = Flask(__name__)
app.config.from_object(Config)

register_blueprints(app)

if __name__ == "__main__":
    app.run(debug=True)
