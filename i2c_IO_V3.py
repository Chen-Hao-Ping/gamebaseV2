import smbus
#from interval import Interval
'''
value ->0 =>請求order     ascii 30
        1 =>請求Frist 裝置 ascii 31
        2 =>請求Secend裝置 ascii 32
        3 =>伺服馬達指令

        65-90 =>大寫英文  
        97-112=>小寫英文 -97  0-26 =>a-z  30-33 =>指令
        ord('a') => 97 
        char(97) => a
        i2c 位元 ->0 -255
'''
bus = smbus.SMBus(1) #set Master
'''
        0 =>請求order     
        1 =>請求Frist 裝置 
        2 =>請求Secend裝置 
        3 =>伺服馬達指令    
'''
def send(address,mode): #傳入地址與資訊 ＃0 or 字母
    try:
        bus.write_byte(int(address), int(mode))
    except:
        print ("Write_except")

'''
def send(address,firstOrSec,value): #傳入地址與資訊 #0 or 字母
    firstOrSec = firstOrSec
    try:
        if firstOrSec == 1:
            bus.write_byte(int(address), int(str(1)+str(ord(value))))
        elif firstOrSec == 2:
            bus.write_byte(int(address), int(str(2)+str(ord(value))))
        elif (type(firstOrSec) == int) & firstOrSec >= 0 & firstOrSec <= 26 & firstOrSec >= 30 & firstOrSec <= 33:
            bus.write_byte(int(address), ord(value))
        else:
            print("firstOrSec type is error")
        print ('raspi2arduino: ', value)
    except:
        print ("Write_except")
'''
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

def Read(address,firstOrSec):
    msg = ""
    try:
        if firstOrSec == 1:
            send(address,1)
            msg = bus.read_byte(int(address))
        elif firstOrSec == 2:
            send(address,2)
            msg = bus.read_byte(int(address))
        if firstOrSec == 0:
            send(address,0)
            msg = bus.read_byte(int(address))
        print ('arduino2raspi:', msg)
    except:
        print ("Read_except")

    return chr(int(msg) + 97)