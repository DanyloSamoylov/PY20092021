class CustomException(Exception):

    def __init__(self, msg, message='dont use uppercase.'):
        self.msg = msg
        self.message = message
        super().__init__(self.message)


try:
    msg = input('Enter anything:')
    if msg.isupper():
        raise CustomException(msg)
except:
    f = open('logs.txt', 'a')
    f.write(f'\nError: {CustomException(msg)}')
    f.close()

