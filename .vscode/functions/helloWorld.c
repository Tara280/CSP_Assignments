#include <stdio.h>

void name(char name[]){
    printf("hello %s\n", name);
}

int main(void){
    name("Elanor");
    name("Karen");
    name("Tyler");
    name("Natalie");
    name("Ben Barnes");
    return 0;
}