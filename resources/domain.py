from flask_jwt import jwt_required
from flask_restful import Resource
from models.domain import DomainModel

class Domain(Resource):

    def get(self, name):
        domain = DomainModel.get_by_name(name)
        if domain:
            return domain.json()
        return {"message": "domain not found"}, 404

class OkList(Resource):
    def get(self, term):
        return {"OK domains": [domain.json() for domain in DomainModel.query.filter(DomainModel.name.like("%{}%".format(term)))]}

class SuspiciousList(Resource):
    def get(self, term):
        return {"Suspicious domains": [domain.json() for domain in DomainModel.query.filter(DomainModel.name.like("%{}%".format(term)))]}

