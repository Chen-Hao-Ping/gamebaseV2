import re
import smbus
import time
#import numpy as np
bus = smbus.SMBus(1) #set Master

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
    

slaveAddressMsg = []
def findAddress(): #return address arrar
    #slaveAddress = [] #slaveAddress ->devicMsg 的物件陣列
    for address in range(1,11):
        try:
            bus.write_byte(int(address),int("0")) #傳入0作為連線判斷及啟動連線
            order = i2cRead(address) #arduino 回傳他目前位置
            slaveAddressMsg.append(deviceMsg(order,address))
        except:
            print("somethong was wrong on address:" +str(address))
    slaveAddressMsg.sort(key=lambda x: x.order)
    return slaveAddressMsg

def sendWord(word):
    word = str(word)
    addressMsg = findAddress()
    errorAddress = []
    if len(word)>len(addressMsg):
        return "len was wrong : word is too long"
    else:
        i = 0
        for address in addressMsg:
            try:
                i2cWrite(address.getAddress(),word[i])
            except:
                print("sent word to arduino was wrong with:"+address)
                errorAddress.append(address)
            i += 1
    return errorAddress #回報錯誤

def getByArduino():
    return slaveAddressMsg

def i2cWrite(address,value): #傳入地址與資訊 ＃0 or 字母
    try:
        bus.write_byte(int(address), ord(value))
        print ('raspi2arduino: ', value)
    except:
        print ("Write_except")

def i2cRead(address):
    msg = ""
    try:
        msg = bus.read_byte(int(address))
        print ('arduino2raspi:', msg)
    except:
        print ("Read_except")
    return msg


if __name__ == '__main__':
    #sendWord("apple")
    i = 3
    while 1:
        i2cWrite(i,'a')
        i2cRead(i)
        i = (i+1)%3
        #time.sleep(1)

#第七次mac test
#第四次PC test