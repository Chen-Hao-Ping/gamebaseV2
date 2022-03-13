class DeviceMsg:
    '''
    def __init__(self, order, address ,word):
        self.__order = order
        self.__address = address
        self.__word = word
    '''
    def __init__(self, order, address):
        self.__order = order
        self.__address = address
    def setWord(self,word):
        self.__word = word
    def setOrder(self,order):
        self.__order = order
    def setAddress(self,address):
        self.__address = address
    
    def setSlaveAddressOrder(self,order,address):
        DeviceMsg.setOrder = order
        DeviceMsg.setAddress = address
    def setErrorSlaveAddressAndWord(self,order,address,word):
        DeviceMsg.setOrder = order
        DeviceMsg.setAddress = address
        DeviceMsg.setWord = word
    
    def getAddress(self):
        return self.__address
    def getOrder(self):
        return self.__order
    def getWord(self):
        return self.__word
    
    def setRespondFrist(self,respondF):
        self.__respondF = respondF

    def getRespondFrist(self):
        return self.__respondF
    
    def setRespondSec(self,respondS):
        self.__respondS = respondS
        
    def getRespondSec(self):
        return self.__respondS