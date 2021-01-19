# flask packages
from flask import Response, request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

# project resources
from models.cafeterias import CafeItems, Cafe
from api.errors import unique_check_route, unauthorized, forbidden

# datetime packages
import datetime
from pytz import timezone
from tzlocal import get_localzone


class CafeteriasCreationAPI(Resource):
    """
        Flask-resftul resource for returning db.cafeterias collection.
    """
    @jwt_required
    def post(self) -> Response:
        """
        POST response method for creating user.
        :return: JSON object
        """
        data = request.get_json()
        post_user = Cafe(**data)
        status = post_user.save()
        if not status:
            return unique_check_route("cafeID ")
        output = {'id': str(post_user.id)}
        return jsonify({'result': output})

    @jwt_required
    def get(self) -> Response:
        """
        GET response method for all documents in cafeterias collection.
        JSON Web Token is required.
        :return: JSON object
        """
        output = Cafe.objects()
        return jsonify({'result': output})

class CreateItemsAPI(Resource):
    """
        Flask-resftul resource for returning db.cafeterias collection.
    """
    @jwt_required
    def post(self) -> Response:
        """
        POST response method for creating user.
        :return: JSON object
        """
        data = request.get_json()
        post_user = CafeItems(**data)
        status = post_user.save()
        if not status:
            return unique_check_route("cafeID")
        output = {'id': str(post_user.id)}
        return jsonify({'result': output})

    @jwt_required
    def get(self) -> Response:
        """
        GET response method for all documents in cafeterias collection.
        JSON Web Token is required.
        :return: JSON object
        """
        output = CafeItems.objects()
        # Current time in UTC
        now_utc = datetime.datetime.now(timezone('UTC'))
        # Convert to local time zone
        now_local = now_utc.astimezone(get_localzone())
        IST = datetime.datetime.strptime(now_local.strftime("%I:%M %p"), "%I:%M %p")
        result = []
        for eachObject in output:
            starttime = datetime.datetime.strptime(eachObject['starttime'], "%I:%M %p")
            endtime = datetime.datetime.strptime(eachObject['endtime'], "%I:%M %p")
            if IST >= starttime and IST <= endtime:
                result.append(eachObject)
        return jsonify({'result': result})


