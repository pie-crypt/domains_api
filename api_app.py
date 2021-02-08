import os
from flask import Flask
from flask_jwt import JWT
from flask_restful import Api
from resources.domain import Domain, OkList, SuspiciousList
from resources.user import UserRegister, User
from security import authenticate, identity
from db import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///db.data')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
db.init_app(app)
app.secret_key = "MY_SECRET_KEY"
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)  #/auth

@app.route('/')
def home():
    return "Hello Domains !"

api.add_resource(Domain, '/domain/<string:name>')
api.add_resource(OkList, '/user_token/ok/<string:term>')
api.add_resource(SuspiciousList, '/user_token/suspicious/<string:term>')
api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>')

if __name__ == '__main__':
    app.run(debug=True)