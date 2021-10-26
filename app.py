from flask import Flask
from models.api_routes import api


app = Flask(__name__)
app.register_blueprint(api)
'''config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))'''
if __name__ == "__main__":
    '''app.config['DEBUG'] = True
    app.config['MONGO_URI'] = config['PROD']['DB_URI']'''
    app.run(debug=True)
