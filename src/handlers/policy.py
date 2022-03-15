from flask import jsonify
from mongoengine.errors import NotUniqueError

from models.policy import Policy
from tools.exceptions import ConflictException, NotFoundException


def get_policy():
    """ Get Policies """
    output = Policy.objects()
    return jsonify({'result': output}), 200


def retrieve_policy(name):
    """ Retrieve policy """

    try:
        policy = Policy.objects.get(name=name)
    except Policy.DoesNotExist:
        raise NotFoundException()

    return jsonify({'result': policy}), 200


def destroy_policy(name):
    """ Destroy policy """

    try:
        ok = Policy.objects(name=name).delete()
        if not ok:
            raise NotFoundException()
    except Policy.DoesNotExist:
        raise NotFoundException()

    return jsonify({}), 204


def create_policy(body: dict):
    """ Create new Policy """
    new_policy = Policy(**body)
    try:
        new_policy.save()
    except NotUniqueError:
        raise ConflictException()
    return jsonify({'result': new_policy}), 201
