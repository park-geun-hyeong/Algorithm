#include<stdio.h>
#include<stdlib.h>
#define size 2

struct school{
    int number;
    char name[20];
    double grade;

};


int main(void){

    int i;

    struct school list[size];

    for(i=0; i<size; i++){
        printf("input number of student : " );
        scanf("%d", &list[i].number);
        printf("input name of student : " );
        scanf("%s", &list[i].name);
        printf("input grade of student : " );
        scanf("%1f", &list[i].grade);
    }

    for(i=0; i<size; i++){
        printf("number: %d, name: %s, grade: %.1f\n", list[i].number,list[i].name, list[i].grade );
    }

    return 0;
};

