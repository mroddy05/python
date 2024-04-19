class Television:
    min_volume = 0
    max_volume = 2
    min_channel = 0
    max_channel = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = self.min_volume
        self.__channel = self.min_channel

    def power(self):
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False

    def mute(self):
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self):
        if self.__status == True:
            if self.__channel == self.max_channel:
                self.__channel = self.min_channel
            else:
                self.__channel += 1

    def channel_down(self):
        if self.__status == True:
            if self.__channel == self.min_channel:
                self.__channel = self.max_channel
            else:
                self.__channel -= 1

    def volume_up(self):
        if self.__status == True:
            if self.__muted == True:
                self.mute()
            if self.__volume == self.max_volume:
                self.__volume = self.max_volume
            else:
                self.__volume += 1

    def volume_down(self):
        if self.__muted == True:
            self.mute()
        if self.__status == True:
            if self.__volume == self.min_volume:
                self.__volume = self.min_volume
            else:
                self.__volume -= 1

    def __str__(self):
        if self.__muted == False:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.min_volume}'
