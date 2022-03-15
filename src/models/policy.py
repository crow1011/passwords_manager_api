from mongoengine import Document, IntField, StringField

DEFAULT_SYMBOLS = """~`! @#$%^&*()_-+={[}]|\:;"'<,>.?/"""
DEFAULT_NUMBERS = "0123456789"
DEFAULT_VOWELS = "AEIOUY"
DEFAULT_CONSONANTS = "BCDFGJKLMNPQSTVXZHRW"

class Policy(Document):
    """ Passwords generation policy model """
    name = StringField(required=True, unique=True)
    password_length = IntField(
        required=False,
        default=16,
        min_value=0)
    symbols = StringField(required=False)
    numbers = StringField(required=False)
    vowels = StringField(required=False)
    consonants = StringField(required=False)
