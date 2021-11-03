import re


class Test():

    def __init__(self, email: str):
        self.email = self.validate(email)

    @classmethod
    def validate(cls, email: str):
        result = '^[a-z0-9]+[\._-]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if not re.search(result, email):
            print('Wrong email name.')
        else:
            print(f'We got your email - {email}')
            return email


Test('danylosamoylov@gmail.com')
