#define _CRT_SECURRE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef struct{
    char name[20];
    int age;
    char address[100];

} Person;

int main(){


    Person *p1 = malloc(sizeof(Person));

    strcpy(p1->name, "park");
    p1->age = 30;
    strcpy(p1->address, "jeonju-si");

    printf("name:%s\n", p1->name);
    printf("age:%d\n", p1->age);
    printf("add:%s\n", p1->address);

    printf("name:%s\n", (*p1).name);
    printf("age:%d\n", (*p1).age);
    printf("add:%s\n", (*p1).address);

    free(p1);

    printf("size of struct:%d", sizeof(Person));
    return 0;
}


