///
/// AirMailShell.c
/// For use on the Raspberry Pi hosted control server
///
/// Created by Tyler Hannis
///
/// Resources
/// http://wiringpi.com/reference/priority-interrupts-and-threads/
/// http://www.raspberry-projects.com/pi/programming-in-c/pipes/named-pipes-fifos
/// https://www.cs.bu.edu/teaching/c/file-io/intro/

//
#include <string.h>

// For configuring the GPIO System
#include <wiringPi.h>

// for the FIFO files
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>


// Defining Pin Numbers to codmatic names
#define fromFlightController 0
#define ServoControl 1

// Defining data file names to codmatic names
#define MAVPROXY_TO_SHELL "/tmp/mavproxy_to_shell"
#define SHELL_TO_MAVPROXY "/tmp/shell_to_mavproxy"
#define ERROR_FILE "/tmp/AirMail_Error.txt"

// Defining function calls
void setupFIFOFiles(NULL);
void closeFIFOFiles(NULL);
int write_SHELL_TO_MAVPROXY(NULL);
int read_MAVPROXY_TO_SHELL(NULL);
void return_error(string x);
void setupGPIO(NULL);
int call_IPS(NULL);


int main(){
    
    /// Calls pin setup function
    setupGPIO();
    
    // FIFO Access/Control variables initialized to negative one
    int SHELL_TO_MAVPROXY_FILESTREAM = -1, MAVPROXY_TO_SHELL_FILESTREAM = -1;
    
    /// constantly running loop
    while(1){
        
        /// interupts waits for the flight controller with indefinite timeout -1
        // static int flightController = waitForInterrupt(fromFlightController, -1);
        
        /// sets the interrupt on pin to specific function call
        // int wiringPiISR (int pin, int edgeType,  void (*function)(void)) ;
                
        /*if(flightController == -1){
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
        */
    }
}

void setupFIFOFiles(NULL){
    
    // --------------------------------------
    // ----- CREATE A FIFO / NAMED PIPE -----
    // --------------------------------------
    int result_SHELL_TO_MAVPROXY, result_MAVPROXY_TO_SHELL;
    
    printf("Making FIFOs...\n");
    /// (These two will fail if the fifo already exists in the system from the app previously running, this is fine)
    result_SHELL_TO_MAVPROXY = mkfifo(SHELL_TO_MAVPROXY, 0777);
    result_MAVPROXY_TO_SHELL = mkfifo(MAVPROXY_TO_SHELL, 0777);
    
    /*
     Note that although this code asks for a mode of 0777, 
     it will be altered by the user mask (umask) setting just as in normal file creation.
     (Shouldn't be an issue since both program are being ran by the same user)
     */

    if (result_SHELL_TO_MAVPROXY == 0)
    {
        // SHELL_TO_MAVPROXY FIFO CREATED
        printf("New FIFO created: %s\n", SHELL_TO_MAVPROXY);
    }
    
    if (result_MAVPROXY_TO_SHELL == 0){
        // MAVPROXY_TO_SHELL FIFO CREATED
        printf("New FIFO created: %s\n", MAVPROXY_TO_SHELL);
    }
    
    // Sets the directions and modes of the FIFO files
    // Each FIFO is unidirectional
    SHELL_TO_MAVPROXY_FILESTREAM = open(SHELL_TO_MAVPROXY, (O_WRONLY));
    MAVPROXY_TO_SHELL_FILESTREAM = open(MAVPROXY_TO_SHELL, (O_RDONLY | O_NONBLOCK));
    
    //  Possible flags:
    //	O_RDONLY - Open for reading only.
    //	O_WRONLY - Open for writing only.
    //	O_NDELAY / O_NONBLOCK (same function) - Enables nonblocking mode. When set read requests on the file can return immediately with a failure status
    //											if there is no input immediately available (instead of blocking). Likewise, write requests can also return
    //											immediately with a failure status if the output can't be written immediately.
    if (SHELL_TO_MAVPROXY != -1)
        printf("Opened FIFO: %i\n", SHELL_TO_MAVPROXY);
    if (MAVPROXY_TO_SHELL != -1)
        printf("Opened FIFO: %i\n", MAVPROXY_TO_SHELL);
}

void closeFIFOFiles(NULL){
    // closes the SHELL_TO_MAVPROXY FIFO
    (void)close(SHELL_TO_MAVPROXY_FILESTREAM);
    // closes the MAVPROXY_TO_SHELL FIFO
    (void)close(MAVPROXY_TO_SHELL_FILESTREAM);
}

int write_SHELL_TO_MAVPROXY(NULL){
    // Setups up a file management data structure
    FILE *fp;
    // configures the File Pointer to write to the SHELL_TO_PROXY FIFO
    fp = fopen(SHELL_TO_MAVPROXY,w);
    return 0;
}

int read_MAVPROXY_TO_SHELL(NULL){
    
    if(MAVPROXY_TO_SHELL_FILESTREAM != -1){
        unsigned char rx_buffer[256];
        int rx_length = read(MAVPROXY_TO_SHELL_FILESTREAM, (void*)rx_buffer, 255);
        // Filestream, buffer to store in, number of bytes to read (max)
        
        if (rx_length < 0){
            // error occured,
            
#if 0
            // DO SOMETHING HERE!
#endif
        }
        
        else if (rx_length == 0){
            // No data waiting
#if 0
            // probably will return a empty value here
#endif
        }
        
        else{
            // info read
            rx_buffer[rx_length] = '\0';
            printf("FIFO %i bytes read : %s\n", rx_length, rx_buffer);
#if 0
            // will probably return a value back into the shell, and switch it
#endif
        }
    }
    return 0;

    
    return 0;
}

/* error return function, flexible */
int return_error(string x){
    error(x);
    exit(1);
}

void setupGPIO(NULL){
    // configures the GPIO pins for the program
    wiringpiSetup()
    // sets pin defined for fromFlightController as a input pin
    pinmode(fromFlightController, input);
    // sets pin defined for ServoControll as an output pin
    pinmode(ServoControl, output);
}

int call_IPS(NULL){
    #if 0
        //call Josh's .py script, return a successful execution
    
        // try to use seperate thread, piThreadCreate
    #endif
    return 0;
}