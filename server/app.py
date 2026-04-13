from flask import Flask, request
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_migrate import Migrate
from models import db, User, Entry

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['JWT_SECRET_KEY'] = '1EBW1y6FHJWZgO0XZSPrG2sqF5qjcBn29eXeeHItRV8'

db.init_app(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)

api = Api(app)

# Authentication Routes
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        return {"token": create_access_token(identity=user.id)}, 200
    return {"message": "Invalid credentials"}, 401

# Resource Endpoints
class EntryResource(Resource):
    @jwt_required()
    def get(self):
        page = request.args.get('page', 1, type=int)
        pagination = Entry.query.filter_by(user_id=get_jwt_identity()).paginate(page=page, per_page=5)
        return [e.to_dict() for e in pagination.items], 200
    
    @jwt_required()
    def post(self):
        data = request.get_json()
        new_entry = Entry(title=data['title'], content=data['content'], user_id=get_jwt_identity())
        db.session.add(new_entry)
        db.session.commit()
        return new_entry.to_dict(), 201

api.add_resource(EntryResource, '/entries')

if __name__ == '__main__':
    app.run(port=5000)