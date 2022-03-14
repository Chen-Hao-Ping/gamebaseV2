#include<Msg.h>
#include <Wire.h>
void setFirstWord(char FirstWord){
  this->FirstWord = FirstWord;
}
void setSecWord(char SecWord){
  this->SecWord = SecWord;
}
char getFirstWord(){
  return this -> FirstWord;
}
char getSecWord(){
  return this -> SecWord;
}
void sendFirstWord(){
  Wire.write(this -> getFirstWord());
}
void sendSecWord(){
  Wire.write(this -> getSecWord());
}

int getOrder(){
  return this ->order;
}
void setOrder(int order){
  //讀取電阻值
}
void sendOrder(){
  Wire.write(this->getOrder());
}
