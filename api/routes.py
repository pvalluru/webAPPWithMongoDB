# flask packages
from flask_restful import Api

# project resources
from api.authentication import SignUpApi, LoginApi
from api.user import UsersApi, UserApi
from api.meal import MealsApi, MealApi
from api.cafeteria import CafeteriasCreationAPI, CafeteriaCreationAPI


def create_routes(api: Api):
    """Adds resources to the api.
    :param api: Flask-RESTful Api Object
    :Example:
        api.add_resource(HelloWorld, '/', '/hello')
        api.add_resource(Foo, '/foo', endpoint="foo")
        api.add_resource(FooSpecial, '/special/foo', endpoint="foo")
    """
    api.add_resource(SignUpApi, '/user/signup/')
    api.add_resource(LoginApi, '/user/login/')

    api.add_resource(UsersApi, '/users/')
    api.add_resource(UserApi, '/users/<user_id>')

    api.add_resource(CafeteriasCreationAPI, '/createcafeteria/')
    api.add_resource(CreateItemsAPI, '/createitems/')
    api.add_resource(CafeteriaCreationAPI, '/createcafeteria/<createcafeteria_id>')