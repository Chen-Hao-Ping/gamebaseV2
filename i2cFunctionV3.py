import i2c_IO as i2c
import i2c_class 
import numpy as np
slaveAddressMsg = []
def findAddress(): #return address arrary
    for address in range(1,7): #12個字母
        try:
            i2c.send(address,0)
            order = i2c.read(address) #arduino 回傳他目前位置
            slaveAddressMsg.append(i2c_class.DeviceMsg(order,address))
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
        i = 1
        for address in addressMsg:
            try:
                i2c.send(address.getAddress(),word[2*i-1])
                i2c.send(address.getAddress(),word[2*i])
            except:
                print("sent word to arduino was wrong with:"+address)
                errorAddress.append(address)
            i += 1
    return errorAddress #回報錯誤

def getArduinoRespond():
    #AnswerRespond = []
    for msg in slaveAddressMsg:
        slaveAddressMsg[slaveAddressMsg.index(msg)].setRespond(i2c.Read(msg.getAddress()))
        slaveAddressMsg[slaveAddressMsg.index(msg)].setRespond(i2c.Read(msg.getAddress()))
        #slaveAddressMsg[msg.getOrder()-1].setRespond(i2c.Read(msg.getAddress()))# i需要變更
    return slaveAddressMsg
'''
def getArduinoRespond():
    AnswerRespond = []
    for address in slaveAddressMsg:
        AnswerRespond.append(DeviceMsg.deviceMsg.setRespond(i2c.Read(address.get)))
    return AnswerRespond
'''

if __name__ == '__main__':
    #sendWord("apple")
    i = 3
    while 1:
        i2c.send(i,'a')
        i2c.read(i)
        i = (i+1)%3
        #time.sleep(1)

#第八次mac test
#第六次PC test