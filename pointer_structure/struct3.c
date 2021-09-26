#include<stdio.h>
#include<stdlib.h>
#include<math.h>


struct point{
    int x;
    int y;

};

void compareStruct(struct point p1, struct point p2){

    if((p1.x==p2.x) && (p1.y == p2.y)){
        printf("two struct is same struct");
    }
}; 

int main(void){

    struct point p1;
    struct point p2;

    p1.x=30;
    p1.y=10;
    p2.x=30;
    p2.y=10;

    compareStruct(p1, p2);

    return 0;

};

