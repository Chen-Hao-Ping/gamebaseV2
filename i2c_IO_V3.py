import smbus

bus = smbus.SMBus(1) #set Master
def send(address,firstOrSec,value): #傳入地址與資訊 ＃0 or 字母
    firstOrSec = firstOrSec
    try:
        if firstOrSec == 1:
            bus.write_byte(int(address), int(str(1)+str(ord(value))))
        elif firstOrSec == 2:
            bus.write_byte(int(address), int(str(2)+str(ord(value))))
        
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