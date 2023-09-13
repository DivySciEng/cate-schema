import os
from flask import Flask, render_template
from flask_swagger_ui import get_swaggerui_blueprint

import os

print("checkpoint 0")
print(__file__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))  
#API_URL = os.path.join(APP_ROOT, 'static/swagger.yaml')

app = Flask(__name__)

# Define your API routes and functions


@app.route("/")
def home():
    return "Hello, World!"

# Serve the Swagger UI interface
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yaml'



swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Swagger UI"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(debug=True)
