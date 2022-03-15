#include<Msg.h>
#include <Wire.h>
void Msg::setFirstWord(char FirstWord){
  FirstWord = FirstWord;
}
void Msg::setSecWord(char SecWord){
  SecWord = SecWord;
}
char Msg::getFirstWord(){
  return FirstWord;
}
char Msg::getSecWord(){
  return SecWord;
}
void Msg::sendFirstWord(){
  Wire.write( getFirstWord());
}
void Msg::sendSecWord(){
  Wire.write( getSecWord());
}

int Msg::getOrder(){
  return order;
}
void Msg::setOrder(int order){
  //讀取電阻值
}
void Msg::sendOrder(){
  Wire.write(getOrder());
}
