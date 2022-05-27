#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){

    char filename[100];
    char s[100];
    for(int i = 0; i<6; i++){
        strcpy(filename, "image");
        sprintf(s, "%d", i);
        strcat(filename, s);
        strcat(filename, ".jpg");
        printf("%s\n", filename);
    }

    return 0;
}

