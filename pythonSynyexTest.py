#import numpy as np
#from https://github.com/Chen-Hao-Ping/gamebaseV2 import i2c_IO
'''
#array = [[0,1],[0,1]]

ar = np.array([[1,1],[4,5],[7,5],[9,7],[2,6],[3,5],[5,5],[8,5],[6,5]])
ar = np.append(ar,[np.array([3,2])],axis = 0)
ar = ar[ar[:, 0].argsort()]'''
'''
print(type(ar[0]))
print(type(ar))
print(type(list(ar[0])))
print(type([1,1]))
print(type(list(ar)))
print(type([np.array([3,2])]))
print(type(np.array([3,2])))
print(type(np.append(ar,[np.array([3,2])],axis = 0)))
'''

'''


word = "apple"
#ar = np.sort(ar, axis = 0)
#ar = ar[:,1]
#errorAddress = np.array([[1,1]])
errorAddress = np.zeros((9,3))
i = 0
for a in word:
    errorAddress = np.append(errorAddress,[np.append(ar[i],[6],axis = 1)],axis = 0)
    i += 1
print(errorAddress)
'''
'''
class address:
    def __init__(self,address,word,sort):
        self.adress = address
        self.word = str(word)
        self.sort  = sort
    def __init__(self,address,word):
        self.adress = address
        self.word = str(word)
    def printMsg(self):
        print(f"{self.adress},{self.word}")    

if __name__ == "__main__":
    address1 = address(0,"b")
    address1.printMsg()
    print(address1.word)
    '''
'''
class Cars: 
        # 建構式
    def __init__(self, color, seat):
        self.color = color  # 顏色屬性
        self.seat = seat  # 座位屬性
    # 方法(Method)
    def drive(self):
        print(f"My car is {self.color} and has {self.seat} seats.")
mazda = Cars("blue", 4)
mazda.drive()'''
'''
class deviceMsg:
    def __init__(self, order, address ,word):
        self.__order = order
        self.__address = address
        self.word = word
    def __init__(self, order, address):
        self.__order = order
        self.__address = address
    def setWord(self,word):
        self.__word = word
    def getWord(self):
        return self.__word

def aa(a):
    return True
if __name__ == "__main__":
    dev = deviceMsg(2,123)
    dev.setWord("a")
    aa()
    print("testA:"+dev.getWord())'''

from i2c_classV3 import DeviceMsg 
if __name__ == "__main__":
    obj = DeviceMsg(1,1)
    print(obj.getOrder())