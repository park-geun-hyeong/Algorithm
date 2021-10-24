#include<stdio.h>
#include<stdlib.h>
#define MAX_DEGREE 101
//#ifdef MAX
#define MAX(a,b) (((a)>(b))?(a):(b))
//#endif // MAX

typedef struct {

    int degree;
    float coef[MAX_DEGREE];
} poly;

// poly a = {5,{10,0,0,0,6,3}};

poly poly_add(poly A, poly B){

    poly C;
    int Apos=0, Bpos=0, Cpos=0;
    int degree_a = A.degree;
    int degree_b = B.degree;
    C.degree = MAX(A.degree,B.degree);


    while(Apos<= A.degree && Bpos<=B.degree){
        if(degree_a > degree_b){
            C.coef[Cpos++] = A.coef[Apos++];
            degree_a--;
        }
        else if(degree_a == degree_b){
            C.coef[Cpos++] = A.coef[Apos++] + B.coef[Bpos++];
            degree_a--;
            degree_b--;

        }
        else if(degree_a < degree_b){
            C.coef[Cpos++] = B.coef[Bpos++];
            degree_b--;
        }

    }

    return C;

}

void print_poly(poly p){

        for(int i = p.degree; i>0; i--){

            printf("%3.1fX^%d + ",p.coef[p.degree - i], i);
        }
        printf("%3.1f\n", p.coef[p.degree]);

}


int main(){

    poly a={5,{2,9,0,3,0,8}};
    poly b={4,{1,0,0,4,5}};
    poly c;
    print_poly(a);
    print_poly(b);

    printf("\n--add poly--\n");
    c = poly_add(a,b);
    print_poly(c);

    return 0;
}

