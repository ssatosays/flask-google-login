from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, id_):
        self.id = id_
