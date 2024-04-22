class Television:
    min_volume: int = 0
    max_volume: int = 2
    min_channel: int = 0
    max_channel: int = 3

    def __init__(self) -> None:
        '''
        Start the initial variables for the Television object
        '''
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.min_volume
        self.__channel: int = Television.min_channel

    def power(self) -> None:
        '''
        Toggle the power status
        '''
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False

    def mute(self) -> None:
        '''
        Toggle the muted status
        '''
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self) -> None:
        '''
        Iterates the channel up by one, wrapping to the beginning when reaching the end
        '''
        if self.__status == True:
            if self.__channel == self.max_channel:
                self.__channel = self.min_channel
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        '''
        Iterates the channel down by one, wrapping to the end when reaching the beginning
        '''
        if self.__status == True:
            if self.__channel == self.min_channel:
                self.__channel = self.max_channel
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        '''
        Iterates the volume up by one, wrapping to the beginning when reaching the end. Does not change when the
        television status is False or off and unmutes if already muted.
        '''
        if self.__status == True:
            if self.__muted == True:
                self.mute()
            if self.__volume == self.max_volume:
                self.__volume = self.max_volume
            else:
                self.__volume += 1

    def volume_down(self) -> None:
        '''
        Iterates the volume down by one, wrapping to the end when reaching the beginning. Does not change when the
        television status is False or off and unmutes if already muted.
        '''
        if self.__muted == True:
            self.mute()
        if self.__status == True:
            if self.__volume == self.min_volume:
                self.__volume = self.min_volume
            else:
                self.__volume -= 1

    def __str__(self) -> str:
        '''
        Retrieve the status, channel, and volume variables of the television object
        :return: a string representing the certain television object
        '''
        if self.__muted == False:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.min_volume}'