#include <stdio.h>
// // #include "cs50.h"
#include "myheaderfile.h"
int main(void) 
{
    // printf("hello, World!\n");

    // // string name = get_string("What is your name? ");
    // // printf("hello", name)

        // OR 

    // Create an array (buffer) to store up to 99 characters for the name
    char name[100]; 
    
    printf("What is your name? ");
    
    // Read the user input until they hit Enter
    scanf("%99s", name); 
    
    printf("hello, %s\n", name);  // %s (String Format Specifier)   // the \n acts one nd like after the name 
    return 0;

        // or 
    
//     char name = get_string("What is your name? ");
//     printf("hello", name); // error
}


