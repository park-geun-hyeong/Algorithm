#include<stdio.h>

void swqp(int *x,int *y){

    int temp;
    temp = *x;
    *x = *y;
    *y = temp;

};

int main(void){

    int x = 1;
    int y = 2;
    printf("Original\nx = %d\ny=%d",x,y);

    swqp(&x, &y);
    printf("\n\nSwap\nx = %d\ny=%d",x,y);
    return 0;
};

