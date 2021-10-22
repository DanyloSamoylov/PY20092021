CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController():

    def __init__(self):
        self.CHANNELS = CHANNELS
        self.current_channel = self.CHANNELS[0]

    def first_channel(self):
        for el, program in enumerate(self.CHANNELS):
            if el == 0:
                print(program)

    def last_channel(self):
        for el, program in enumerate(self.CHANNELS):
            if program in self.CHANNELS[-1]:
                print(program)

    def turn_channel(self, x):
        for el, program in enumerate(self.CHANNELS):
            if x == el + 1:
                print(program)

    def next_channel(self):
        i = self.CHANNELS.index(self.current_channel)
        if i == len(self.CHANNELS) - 1:
            self.current_channel = self.CHANNELS[0]
            print(self.current_channel)
        else:
            self.current_channel = self.CHANNELS[i+1]
            print(self.current_channel)

    def previous_channel(self):
        i = self.CHANNELS.index(self.current_channel)
        if i == 0:
            self.current_channel = self.CHANNELS[-1]
            print(self.current_channel)
        else:
            self.current_channel = self.CHANNELS[i-1]
            print(self.current_channel)

    def current_channel(self):
        print(self.current_channel)

    def is_exist(self, x):
        if x in self.CHANNELS or 0 <= int(x) < len(self.CHANNELS):
            return print(f'Yes "{x}" is exist.')
        else:
            return print(f'No "{x}" is not exist.')


controller = TVController()

controller.first_channel()
controller.last_channel()
controller.turn_channel(1)
controller.next_channel()
controller.previous_channel()
# controller.current_channel()
controller.is_exist(4)
controller.is_exist("BBC")

