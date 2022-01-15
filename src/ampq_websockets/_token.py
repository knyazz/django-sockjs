import hashlib

from _settings import SECRET_KEY


class Token:
    def get_secret_data(self, data: str) -> str:
        token = SECRET_KEY + data
        return hashlib.md5(token.encode()).hexdigest()

    def get_data(self, token: str, data: str) -> str:
        if token != self.get_secret_data(data):
            raise KeyError
        return data
