#include<stdio.h>

int foo(int n){

    if(n==0) return 1;
    if(n==1) return 2;

    int an = foo(n-1) + 2*foo(n-2);

    return an;
}

int foo2(int n){

     int arr[n+1];

     arr[0] = 1;
     arr[1] = 2;

     for(int i =2; i < n+1; i++){
        arr[i] = arr[i-1] + 2*arr[i-2];
        }

     return arr[n];
}


int main(){

    printf("recursive:");
    for(int i=0; i<11; i++){
        int an = foo(i);
        printf("%d ", an);
    }

    printf("\ndynamic: ");
    for(int i=0; i<11; i++){
        int an = foo2(i);
        printf("%d ", an);
    }


    return 0;
}

