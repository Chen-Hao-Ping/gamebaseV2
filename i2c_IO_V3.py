import smbus
'''
value ->0 =>請求order     ascii 30
        1 =>請求Frist 裝置 ascii 31
        2 =>請求Secend裝置 ascii 32
        65-90 =>大寫英文  
        97-112=>小寫英文 -97  0-26 =>a-z  30-32 =>指令
        ord('a') => 97 
        char(97) => a
        i2c 位元 ->0 -255
'''
bus = smbus.SMBus(1) #set Master
def send(address,firstOrSec,value): #傳入地址與資訊 ＃0 or 字母
    firstOrSec = firstOrSec
    try:
        if firstOrSec == 1:
            bus.write_byte(int(address), int(str(1)+str(ord(value))))
        elif firstOrSec == 2:
            bus.write_byte(int(address), int(str(2)+str(ord(value))))
        elif (type(firstOrSec) == int) & :
            bus.write_byte(int(address), ord(value))
        else:
            print("firstOrSec type is error")
        print ('raspi2arduino: ', value)
    except:
        print ("Write_except")
'''
def ReadF(address):
    msg = ""
    try:
        send(address,'1')
        msg = bus.read_byte(int(address))
        print ('arduino2raspi:', msg)
    except Exception as e:
        print ("Read_except -" + e)
    return msg
'''
'''
def ReadS(address):
    msg = ""
    try:
        send(address,'2')
        msg = bus.read_byte(int(address))
        print ('arduino2raspi:', msg)
    except Exception as e:
        print ("Read_except -" + e)
    return msg
'''

def Read(address):
    msg = ""
    try:
        msg = bus.read_byte(int(address))
        print ('arduino2raspi:', msg)
    except:
        print ("Read_except")
    return msg