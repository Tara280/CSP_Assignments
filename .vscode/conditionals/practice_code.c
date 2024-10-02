#include <stdio.h>

int num = 4;

int main(){ 
    if (num < 10){
        printf("This is a single digit number\n");
    }else if (num < 100){
        printf("This is a double digit number\n");
    }else{
        printf("THis is at least a tripple digit number\n");
    }

    return 0;
}