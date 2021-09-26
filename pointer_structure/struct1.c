#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>

struct student{
    int number;
    char name[10];
    double grade;
};

struct point{

    int x;
    int y;

};

int main(void ){

    struct student s;
    struct point p1, p2;


    //s.number = 2020;
    //strcpy(s.name, "park");
    //s.grade =4.5;
    //printf("number : %d, name : %s, grade : %.1f", s.number, s.name, s.grade);

    printf("input p1 point : ");
    scanf("%d %d", &p1.x, &p1.y);
    printf("input p2 point : ");
    scanf("%d %d", &p2.x, &p2.y);

    int xdiff = p1.x - p2.x;
    int ydiff = p1.y - p2.y;

    printf("distance : %.4f", sqrt(xdiff*xdiff + ydiff*ydiff));

    return 0;

};

