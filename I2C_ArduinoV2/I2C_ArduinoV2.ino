#include <Wire.h>
/*
'''
value ->0 =>請求order     ascii 30
        1 =>請求Frist 裝置 ascii 31
        2 =>請求Secend裝置 ascii 32
        3 =>伺服馬達指令

        65-90 =>大寫英文  
        97-112=>小寫英文 -97  0-26 =>a-z  30-33 =>指令
        ord('a') => 97 
        char(97) => a
        i2c 位元 ->0-255
'''
*/
int SLAVE_ADDRESS = 1;  // 設定Arduino開發板I2C的位址
int number = 255;
char firstWord = 0;
char secWord = 0;
class Msg{
  public:
    void setFirstWord(int);//1XX // 玩家
    void setSecWord(int);//2XX   // 玩家
    char getFirstWord(void);//+97
    char getSecWord(void);//+97
    void setFirstServus(int);
    void setSecServus(int);
   private:
    char FirstWord;//讀到得值
    char SecWord;  //讀到得值
    
    
  };
class DeviceMsg{
  public:
    void setOrder(int);
    int getOrder(void);
    void sendword(void);
  private:
    int order;      
  };


void Msg::setFirstWord(int FirstWord){ //FirstWord => 電阻值 
  this->FirstWord = (FirstWord - 100) + 97;
}
void Msg::setSecWord(char SecWord){
  this->SecWord = (SecWord - 200) + 97;;
}
char Msg::getFirstWord(){
  
  return this -> FirstWord;
}
char Msg::getSecWord(){
  return this -> SecWord;
}



void DeviceMsg::setOrder(int order){
  this ->order = order;
}
int DeviceMsg::getOrder(){
  return this->order;
}
vodid DeviceMsg::sendword(){

}

Msg msg;

DeviceMsg DM;

void setup() {
  //i2cFuction i2cF();
  Serial.begin(9600);   // Serial通訊埠通訊設為9600速率
  Wire.begin(SLAVE_ADDRESS);  // 初始化Arduino的I2C位址
  
  Wire.onReceive(receiveData); //I2C訊號接收時，啟用函式
  
  Wire.onRequest(sendData);  //主機要求讀取時，啟用函式
}

void loop() {
  
}

void getFirst(){
  
  }
void getSec(){
  
  }
void receiveData(int byteCount){
while(Wire.available()) {
    //當I2C的buffer中有資料時進入迴圈
  number = Wire.read();   //指定nubmer 等於讀取的訊息
  if(number>=100 && number<200){
    getFirst();
    }else if(number>=200){
      getSec();
      }else if(number == 255){
        Serial.println("something is wrong!");
        }else if(number == 30){
          //請求order
          }else if(number == 31){
            //請求First卡槽
            }else if(number == 32){
              //請求Sec卡槽
             }else if(number == 33){
              //全部動作
              }
  Serial.print("data received: ");
  Serial.println(number);
  }
}
void sendData(){
    number = Wire.read();
    
    if(number == 1){
      
      msg.getFirstWord();
      }else if(number == 2){
        msg.getSecWord();
        }
    Wire.write(SLAVE_ADDRESS);
    Wire.begin(SLAVE_ADDRESS); 
}
