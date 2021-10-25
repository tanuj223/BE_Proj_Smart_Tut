from flask import Flask
import os
from api_routes import api
import configparser


app = Flask(__name__)
app.register_blueprint(api)
'''config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))'''
if __name__ == "__main__":
    '''app.config['DEBUG'] = True
    app.config['MONGO_URI'] = config['PROD']['DB_URI']'''
    app.run(debug=True)
