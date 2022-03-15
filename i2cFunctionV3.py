import i2c_IO_V3 as i2c
#from i2c_classV3 import DeviceMsg 
import i2c_classV3 as claI2c
slaveAddressMsg = []
def findAddress(): #return address arrary
    for address in range(1,7): #12個字母
        try:
            i2c.send(address,0)
            order = i2c.Read(address,0) #arduino 回傳他目前位置
            obj = claI2c.DeviceMsg(order,address)
            slaveAddressMsg.append(claI2c(order,address))
        except:
            print("somethong was wrong on address:" +str(address))
    slaveAddressMsg.sort(key=lambda x: x.order)
    return slaveAddressMsg
'''
def sendWord(word):
    word = str(word)
    addressMsg = findAddress()
    errorAddress = []
    if len(word)>len(addressMsg)*2:
        return "len was wrong : word is too long"
    else:
        i = 0
        for address in addressMsg:
            try:
                i2c.send(address.getAddress(),1,word[i*2])
                i2c.send(address.getAddress(),2,word[i*2+1])
            except:
                print("sent word to arduino was wrong with:"+address)
                errorAddress.append(address)
            i += 1
    return errorAddress #回報錯誤
'''
def getArduinoRespond():
    #AnswerRespond = []
    '''=======================================''' #必須修改ＩＯ 
    for msg in slaveAddressMsg:
        slaveAddressMsg[slaveAddressMsg.index(msg)].setRespondFrist(i2c.Read(msg.getAddress(),1))
        slaveAddressMsg[slaveAddressMsg.index(msg)].setRespondSec(i2c.Read(msg.getAddress(),2))
        #slaveAddressMsg[msg.getOrder()-1].setRespond(i2c.Read(msg.getAddress()))# i需要變更
    return slaveAddressMsg
'''
def getArduinoRespond():
    AnswerRespond = []
    for address in slaveAddressMsg:
        AnswerRespond.append(DeviceMsg.deviceMsg.setRespond(i2c.Read(address.get)))
    return AnswerRespond
'''
