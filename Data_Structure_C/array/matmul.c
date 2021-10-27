#include<stdio.h>
#include<stdlib.h>
#define DIM 3

int main(){

    int A[DIM][DIM] = {0};
    int B[DIM][DIM] = {0};
    int C[DIM][DIM] = {0};
    int i,j,k;

    for(i=0; i<DIM; i++){
        printf("Input row %d of matrix A:",i);
        scanf("%d %d %d", &A[i][0], &A[i][1], &A[i][2]);
    }

    for(i=0; i<DIM; i++){
        printf("Input row %d of matrix B:",i);
        scanf("%d %d %d", &B[i][0], &B[i][1], &B[i][2]);
    }

    printf("Matrix A:\n");
    for(i=0; i<DIM; i++){
        printf("%d %d %d\n", A[i][0],A[i][1],A[i][2]);
    }
    printf("Matrix B:\n");
    for(i=0; i<DIM; i++){
        printf("%d %d %d\n", B[i][0],B[i][1],B[i][2]);
    }
    printf("Matrix C = A x B:\n");


    for(i=0; i<DIM; i++){
        for(j=0; j<DIM; j++){
            int ans = 0;
            for(k=0; k<DIM; k++){
                ans = ans + (A[i][k] * B[k][j]);
            }
            C[i][j] = ans;
        }
    }

    for(i=0; i<DIM; i++){
        printf("%d %d %d\n", C[i][0],C[i][1],C[i][2]);
    }

    return 0;
}

