import smbus

bus = smbus.SMBus(1) #set Master
def send(address,value): #傳入地址與資訊 ＃0 or 字母
    '''
    value ->0 =>請求order
            1 =>請求Frist 裝置
            2 =>請求Secend裝置
            65-90 =>大寫英文
            97-112=>小寫英文
            ord('a') => 97 
            char(97) => a
            i2c 位元 ->0 -255

    '''
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
  