#ifndef Msg_h
#define Msg_h

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

#endif