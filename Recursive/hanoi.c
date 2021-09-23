#include <stdio.h>

void move(int n, char start, char end){
    printf("move %d disk, from %c to %c \n", n, start, end);
};

void hanoi(int n, char start, char via, char end){
    if(n == 1){
            move(n, start, end);}
    else{
        hanoi(n-1, start, end, via);
        move(n, start ,end);
        hanoi(n-1, start, via, end);}
};

void main(){

    int N;
    scanf("%d", &N);
    hanoi(N, 'a', 'b', 'c');
    return 0;

};


