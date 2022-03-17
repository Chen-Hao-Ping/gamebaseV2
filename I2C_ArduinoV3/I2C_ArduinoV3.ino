#include <Wire.h>
#include <SCoop.h>
#include <Msg.h>

/*
'''
value ->0 =>請求order     
        1 =>請求Frist 裝置 
        2 =>請求Secend裝置
        3 =>伺服馬達指令

        65-90 =>大寫英文  
        97-112=>小寫英文 -97  0-26 =>a-z  30-33 =>指令
        ord('a') => 97 
        char(97) => a
        i2c 位元 ->0-255
'''
*/
int SLAVE_ADDRESS = 3;  // 設定Arduino開發板I2C的位址
int number = 255;
char firstWord = 255;
char secWord = 255;
/*
class Msg{
  public:
    void setFirstWord(char);//1XX
    void setSecWord(char);//2XX
    char getFirstWord(void);//+97
    char getSecWord(void);//+97
    void sendFirstWord(void);
    void sendSecWord(void);
    void setOrder(int);
    int getOrder(void);
    void sendOrder(void);
  private:
    char FirstWord;
    char SecWord;  
    int order;
  };

  


void Msg::setFirstWord(char FirstWord){
  this->FirstWord = FirstWord;
}
void Msg::setSecWord(char SecWord){
  this->SecWord = SecWord;
}
char Msg::getFirstWord(){
  return this -> FirstWord;
}
char Msg::getSecWord(){
  return this -> SecWord;
}
void Msg::sendFirstWord(){
  Wire.write(this -> getFirstWord());
}
void Msg::sendSecWord(){
  Wire.write(this -> getSecWord());
}

int Msg::getOrder(){
  return this ->order;
}
void Msg::setOrder(int order){
  //讀取電阻值
}
void Msg::sendOrder(){
  Wire.write(this->getOrder());
}
*/
Msg msg;

//int waitSend = 255;
void receiveData(int byteCount){
  while(Wire.available()) {
    number = Wire.read();   //指定nubmer 等於讀取的訊息
    Serial.print("data received: ");
    Serial.println(number);
  }
}
void sendData(){
    //number = Wire.read();
    if(number == 1){
      
      msg.setFirstWord(SLAVE_ADDRESS+10);//引數為讀取一號角位值

      msg.sendFirstWord();
      Serial.print("on1");
      //Wire.write(97);
      }else if(number == 2){
      
        msg.setSecWord(SLAVE_ADDRESS+11);//引數為讀取一號角位值

        msg.sendSecWord();
        Serial.print("on2");
        //Wire.write(98);
        }else if(number == 0){
          
          msg.setOrder(SLAVE_ADDRESS);//引數為讀取一號角位值(順序)
          Serial.print(msg.getOrder());
          //Wire.write(SLAVE_ADDRESS);
          msg.sendOrder();
          
          }else if(number == 3){

            //伺服馬達動作
          }
}  

defineTask(I2c); 
  void I2c::setup() {

    Serial.begin(9600);   // Serial通訊埠通訊設為9600速率
    
    Wire.begin(SLAVE_ADDRESS);  // 初始化Arduino的I2C位址
    
    Wire.onReceive(receiveData); //I2C訊號接收時，啟用函式
    
    Wire.onRequest(sendData);  //主機要求讀取時，啟用函
  } 
  void I2c::loop() {
    
  } 

defineTask(servusControl); 
  void servusControl::setup() {
    //一般伺服馬達動作及其他指令設定之setup;
  }

  void servusControl::loop() {
    //一般伺服馬達動作及其他指令設定之loop;
  } 


void setup() {
  Serial.print("already");
  mySCoop.start(); 
  /*Serial.begin(9600);   // Serial通訊埠通訊設為9600速率
    
    Wire.begin(SLAVE_ADDRESS);  // 初始化Arduino的I2C位址
    
    Wire.onReceive(receiveData); //I2C訊號接收時，啟用函式
    
    Wire.onRequest(sendData);  //主機要求讀取時，啟用函式*/
}

void loop(){
  yield();
  //delay(100);
}
