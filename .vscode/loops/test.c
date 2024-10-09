#include <stdio.h>

char sibs[3][20] = {"Maiah", "Alaiah", "Kaylee"};
int i;
int main (){
   while(i<10){
        printf("%s\n", sibs[i]);
        i++;
   }
}