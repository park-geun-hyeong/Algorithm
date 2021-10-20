#include<stdio.h>

typedef struct{

    int x;
    int y;

} point2d;

int main(){

    int i;

    point2d p[3] = {{1,2},{3,4},{5,6}} ;

    point2d *ptr[3];

    for(i=0; i<3; i++){

        ptr[i] = malloc(sizeof(point2d));

    }

    ptr[0]->x = 10;
    ptr[0]->y = 20;

    ptr[1]->x = 10;
    ptr[1]->y = 20;

    ptr[2]->x = 10;
    ptr[2]->y = 20;

    printf("%d %d\n", p[0].x, p[0].y);
    printf("%d %d\n", p[1].x, p[1].y);
    printf("%d %d\n", p[2].x, p[2].y);


    printf("%d %d\n", ptr[0]->x, ptr[0]->y);
    printf("%d %d\n", ptr[1]->x, ptr[1]->y);
    printf("%d %d\n", ptr[2]->x, ptr[2]->y);


    for(i=0; i<3; i++){
        free(ptr[i]);
    }

    return 0;

}

