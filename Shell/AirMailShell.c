///
/// AirMailShell.c
/// For use on the Raspberry Pi hosted controll server
///
/// Created by Tyler Hannis
///
/// Resources
/// http://wiringpi.com/reference/priority-interrupts-and-threads/

#include <stdio.h>
#include <string.h>
#include <wiringPi.h>


// Defining Pin Numbers to codmatic names
#define fromFlightController 0
#define ServoControll 1

int main(){
    // Calls pin setup function
    setupPins();
    // constantly running loop
    while(1){
        // interupts waits for the flight controller with indefinite timeout -1
        static int flightController = waitForInterrupt(fromFlightController, -1);
        
        // int wiringPiISR (int pin, int edgeType,  void (*function)(void)) ;
        // sets the interrupt on pin to specific function call
        
        if(flightController == -1){
            // errno will still be set appropriately on error
            return_error("Error in flightController interrrupt");
            
        #if 0
            // action required here in event that error returned is acceptable
        #endif
        }
        elseif(flightController = 0){
            #if 0
                // this check can possibly be deleted later
                // checks to see if interrupt timed out
                // (not sure how this will be handled yet)
            #endif
        }
        
        elseif(flightController = 0){
            
        }
        flightController = 0;
    }
}

int return_error(string x){
    error(x);
    exit(1);
}

void setupPins(NULL){
    // configures the GPIO pins for the program
    wiringpiSetup()
    // sets pin defined for fromFlightController as a input pin
    pinmode(fromFlightController, input);
    // sets pin defined for ServoControll as an output pin
    pinmode(ServoControll, output);
}

int call_IPS(NULL){
    #if 0
        //call Josh's .py script, return a successful execution
    
        // try to use seperate thread, piThreadCreate
    #endif

}