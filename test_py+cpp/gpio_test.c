#include <wiringPi.h>    
#include<stdio.h>
#include<softPwm.h>

int ini(void);
void pySet_PinMode(int pin_number,int mode);
int pyDigitalRead(int pin);
void pyDigitalWrite(int pin,int value);
int pySoftPwmCreate(int pin,int initialValue,int pwmRange);
void pySoftPwmWrite(int pin,int value);
void interrupt_counter(void);
void pySetInterrupt(int pin,int mode);
int pyReadInterruptCounter(void);
int pyReadDuration(void);
struct return_value_struc pyReturnStructure(void);

int value_inter=0;
unsigned int last_micro=0;
unsigned int this_micro=0;
unsigned int duration=0;
struct return_value_struc{
	int duration;
	int value_inter;

};

struct return_value_struc return_value={0,0};

int ini(void)    
{    
	//return wiringPiSetup() ;
	return wiringPiSetupPhys();
}


void pySet_PinMode(int pin_number,int mode){
	pinMode (pin_number,mode ) ;    
}

int pyDigitalRead(int pin){
	int temp=digitalRead(pin);
	return temp;
}   

void pyDigitalWrite(int pin,int value){
	digitalWrite(pin,value);
}   

int pySoftPwmCreate(int pin,int initialValue,int pwmRange){
	return softPwmCreate(pin,initialValue,pwmRange);
}
void pySoftPwmWrite(int pin,int value){
	softPwmWrite(pin,value);

}
void interrupt_counter(void){
	this_micro=micros();
	value_inter++;
	duration=this_micro-last_micro;
	last_micro=micros();
}


void pySetInterrupt(int pin,int mode){
	wiringPiISR(pin,mode,&interrupt_counter);

}

int pyReadInterruptCounter(void){
	return value_inter;
}

int pyReadDuration(void){
	return duration;

}

struct return_value_struc pyReturnStructure(void){
	return_value.duration=duration;
	return_value.value_inter;
	return return_value;
}

