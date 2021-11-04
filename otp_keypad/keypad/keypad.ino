#include <Keypad.h>

const byte ROWS = 4; //four rows
const byte COLS = 3; //three columns
char keys[ROWS][COLS] = {
  {'1','2','3'},
  {'4','5','6'},
  {'7','8','9'},
  {'*','0','#'}
};
byte rowPins[ROWS] = {7,2,3,5}; //connect to the row pinouts of the keypad
byte colPins[COLS] = {6,8,4}; //connect to the column pinouts of the keypad

Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );

void setup(){
  Serial.begin(9600);
  
}
int count = 0; 
void loop(){
  char key = keypad.getKey();
  char password[6];
  
  if (key && (count<6)){
    Serial.println(key);
    password[count]=key;
    count++;
    if(count==6){
      Serial.println(password);
    }
    else if (count>6){
      exit(0);
    }
  }
}
