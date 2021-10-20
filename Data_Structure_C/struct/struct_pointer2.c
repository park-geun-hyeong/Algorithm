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


    Person p1;
    Person *ptr; //not use malloc

    ptr = &p1; //struct pointer ptr에 p1의 주소 할당

    strcpy(ptr->name, "park");
    ptr->age = 30;
    strcpy(ptr->address, "jeonju-si");

    printf("name:%s\n", ptr->name);
    printf("age:%d\n", ptr->age);
    printf("add:%s\n", ptr->address);

    printf("name:%s\n", p1.name);
    printf("age:%d\n", p1.age);
    printf("add:%s\n", p1.address);

    return 0;
}


