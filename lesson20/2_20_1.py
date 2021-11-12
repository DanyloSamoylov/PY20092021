import datetime as dt


class OpenCounter:
    _counter = 0

    def __init__(self, file, mode, log_file='logs.log', log_mode='a'):
        self.mode = mode
        self.file = file
        self.log_file = log_file
        self.log_mode = log_mode

    def __enter__(self):
        self.fd = open(self.file, self.mode)
        self.__class__._counter += 1
        self._write_logs()
        return self.fd

    def __exit__(self, exc_type, exc_val, exc_tb):
        return None

    def _write_logs(self):
        with open(self.log_file, self.log_mode) as logs:
            logs.write(f'{dt.datetime.now()}: {self._counter} time(s)\n')

    def get_counter_number(self):
        return self._counter


with OpenCounter('any_text.txt', 'a') as text_file:
    text_file.write('some text')

with OpenCounter('any_text.txt', 'a') as text_file:
    text_file.write('some text')

with OpenCounter('any_text.txt', 'a') as text_file:
    text_file.write('some text')
