import smbus

bus = smbus.SMBus(1) #set Master
def send(address,value): #傳入地址與資訊 ＃0 or 字母
    try:
        bus.write_byte(int(address), ord(value))
        print ('raspi2arduino: ', value)
    except:
        print ("Write_except")

def ReadF(address):
    msg = ""
    try:
        msg = bus.read_byte(int(address))
        print ('arduino2raspi:', msg)
    except:
        print ("Read_except")
    return msg
    
def ReadS(address):
    msg = ""
    try:
        msg = bus.read_byte(int(address))
        print ('arduino2raspi:', msg)
    except:
        print ("Read_except")
    return msg

def Read(address):
    msg = ""
    try:
        msg = bus.read_byte(int(address))
        print ('arduino2raspi:', msg)
    except:
        print ("Read_except")
    return msg
  