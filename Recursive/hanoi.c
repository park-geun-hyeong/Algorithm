#include <stdio.h>

void move(int n, char start, char end){
    printf("move %d disk, from %c to %c \n", n, start, end);
};

void hanoi(int n, char start, char end, char via){
    if(n == 1){
            move(1, start, end);}
    else{
        hanoi(n-1, start, via, end);
        move(n, start ,end);
        hanoi(n-1, via, end, start);}
};

void main(){

    int N;
    scanf("%d", &N);
    hanoi(N, 'a', 'c', 'b');
    return 0;

};




