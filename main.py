import gttsFunction as gF
import i2cFunctionV2 as i2c
if __name__ == '__main__':
	#print("Hello word")
	#gF.speak("apple",'en')
	#sendWord("apple")
	i = 3
	while 1:
		i2c.sendWord("apple")
		i2c.getRespond()
		
        #time.sleep(1)