#include <Wire.h>

int SLAVE_ADDRESS = 1;  // 設定Arduino開發板I2C的位址
int number = 255;
char firstWord = 0;
char secWord = 0;
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
    Wire.write(SLAVE_ADDRESS);
    Wire.begin(SLAVE_ADDRESS); 
}
