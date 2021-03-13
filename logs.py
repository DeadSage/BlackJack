import time
import datetime
from traceback import format_exc as tb


class Logs:

    def __init__(self, file_name):
        self.logs_dir = ''
        self.file_name = file_name
        self.path = f"{self.logs_dir}{self.file_name}"

    def trace(self, info):
        with open(self.path, 'a') as file:
            file.write(self.forming(info))

    def forming(self, info):
        trb = tb() if tb()[:4] != 'None' else ''
        template = f"{self.cur_time()}: {info}\n{trb}"
        return template

    def cur_time(self):
        return datetime.datetime.isoformat(datetime.datetime.now(), sep=' ')


log = Logs('BlackJack.log')
tb()
log.cur_time()

