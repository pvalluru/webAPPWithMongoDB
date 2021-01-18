# flask packages
from flask import Response, request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

# project resources
from models.cafeterias import Cafeterias
from api.errors import forbidden, unique_check_route


class CafeteriasCreationAPI(Resource):
    """
        Flask-resftul resource for returning db.meal collection.
    """
    @jwt_required
    def post(self) -> Response:
        """
        POST response method for creating user.
        :return: JSON object
        """
        data = request.get_json()
        post_user = Cafeterias(**data)
        status = post_user.save()
        if not status:
            return unique_check_route()
        output = {'id': str(post_user.id)}
        return jsonify({'result': output})

    @jwt_required
    def get(self) -> Response:
        """
        GET response method for all documents in meal collection.
        JSON Web Token is required.
        :return: JSON object
        """
        output = Cafeterias.objects()
        return jsonify({'result': output})


class CafeteriaCreationAPI(Resource):
    """
    Flask-resftul resource for returning db.meal collection.
    """
    @jwt_required
    def get(self, meal_id: str) -> Response:
        """
        GET response method for single documents in meal collection.
        :return: JSON object
        """
        output = Cafeterias.objects.get(id=meal_id)
        return jsonify({'result': output})

    @jwt_required
    def put(self, meal_id: str) -> Response:
        """
        PUT response method for updating a meal.
        JSON Web Token is required.
        Authorization is required: Access(admin=true)
        :return: JSON object
        """
        data = request.get_json()
        put_user = Cafeterias.objects(id=meal_id).update(**data)
        return jsonify({'result': put_user})

    @jwt_required
    def delete(self, user_id: str) -> Response:
        """
        DELETE response method for deleting single meal.
        JSON Web Token is required.
        Authorization is required: Access(admin=true)
        :return: JSON object
        """
        authorized: bool = Cafeterias.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            output = Cafeterias.objects(id=user_id).delete()
            return jsonify({'result': output})
        else:
            return forbidden()