from mongoengine import Document, StringField


class Password(Document):
    """ Password Model """
    password_hash = StringField()
