#include<stdio.h>
#include<ctype.h>

char s[] = "Man is immortal, because he has a soul";
char seps[] = " ,\n\t";
char *token;


int main(){

    token = strtok(s, seps);
    while(token != NULL){

        printf("token : %s\n", token);
        token = strtok(NULL, seps);
    }

    return 0;
}




