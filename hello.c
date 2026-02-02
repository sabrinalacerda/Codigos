#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    // Prompt user for their name
    char name = get_char("What is your name? ");

    // Greet the user
    printf("Hello, %c!\n", name);

    return 0;
}