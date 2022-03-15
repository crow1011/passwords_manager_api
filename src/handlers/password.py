from flask import jsonify

from models.policy import Policy
from tools.exceptions import NotFoundException
from tools.pwd_gen import generate_password


def get_password(policy_name):
    """ Create password by Policy """

    try:
        policy = Policy.objects.get(name=policy_name)
    except Policy.DoesNotExist:
        raise NotFoundException()

    new_password, _ = generate_password(
        name=policy.name,
        password_length=policy.password_length,
        symbols = policy.symbols,
        numbers = policy.numbers,
        vowels = policy.vowels,
        consonants = policy.consonants
    )
    return jsonify({"result": {"passord": new_password}})
