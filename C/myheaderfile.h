#include <stdio.h>
#include <stdlib.h> // Required for malloc and free

// Modified prototype to take only ONE argument
char* get_string(char* prompt);

int main(void)
{
    // Now you call it exactly like CS50!
    char* name = get_string("What is your name? ");
    
    // Check if memory allocation failed
    if (name == NULL) 
    {
        return 1; 
    }

    printf("hello, %s\n", name);
    
    // Always free memory allocated with malloc when you are done using it
    free(name); 
    return 0;
}

// Updated function definition
char* get_string(char* prompt)
{
    printf("%s", prompt);
    
    // Allocate space for 100 characters on the heap memory
    char* buffer = malloc(100 * sizeof(char));
    if (buffer == NULL) 
    {
        return NULL; // Return NULL if the computer runs out of memory
    }
    
    // Read user input (%99s prevents buffer overflow inside our 100-byte space)
    scanf("%99s", buffer); 
    
    return buffer;
}
