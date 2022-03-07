class deviceMsg:
    def __init__(self, order, address ,word):
        self.__order = order
        self.__address = address
        self.__word = word
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
        deviceMsg.setOrder = order
        deviceMsg.setAddress = address
    def setErrorSlaveAddressAndWord(self,order,address,word):
        deviceMsg.setOrder = order
        deviceMsg.setAddress = address
        deviceMsg.setWord = word
    
    def getAddress(self):
        return self.__address
    def getOrder(self):
        return self.__order
    def getWord(self):
        return self.__word
    
    def setRespond(self,respond):
        self.__respond = respond
    def getRespond(self):
        return self.__respond
    