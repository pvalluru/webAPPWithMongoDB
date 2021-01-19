# flask packages
from flask_restful import Api

# project resources
from api.authentication import SignUpApi, LoginApi
from api.user import UsersApi
from api.cafeteria import CafeteriasCreationAPI, CreateItemsAPI


def create_routes(api: Api):
    """Adds resources to the api.
    :param api: Flask-RESTful Api Object
    """
    api.add_resource(SignUpApi, '/user/signup/')
    api.add_resource(LoginApi, '/user/login/')

    api.add_resource(UsersApi, '/users/')

    api.add_resource(CafeteriasCreationAPI, '/createcafeteria/')
    api.add_resource(CreateItemsAPI, '/createcafeteriaitems/')
