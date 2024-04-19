class Television:
    min_volume = 0
    max_volume = 2
    min_channel = 0
    max_channel = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = self.min_volume
        self.channel = self.min_channel

    def power(self):
        if self.status == False:
            self.status = True
        else:
            self.status = False

    def mute(self):
        if self.muted == False:
            self.muted = True
        else:
            self.muted = False

    def channel_up(self):
        if self.channel == self.max_channel:
            self.channel = self.min_channel
        else:
            self.channel += 1

    def channel_down(self):
        if self.channel == self.min_channel:
            self.channel = self.max_channel
        else:
            self.channel -= 1

    def volume_up(self):
        if self.volume == self.max_volume:
            self.volume = self.max_volume
        else:
            self.volume += 1

    def volume_down(self):
        if self.volume == self.min_volume:
            self.volume = self.min_volume
        else:
            self.volume -= 1

    def __str__(self):
        return f'Power = {self.status}, Channel = {self.channel}, Volume = {self.volume}'
