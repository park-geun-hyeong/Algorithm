#include<stdio.h>
#include<math.h>


int main(){
    // 소수는 1과 자기자신만을 약수로 가지는 숫자

    int n,i;

    while(1){
        int flag = 0;
        printf("정수를 입력하세요: ");
        scanf("%d",&n);
        if(n<0){goto END;}

        for(i=2; i<=sqrt(n); i++){
            if(n%i == 0){
                flag = 1;
                break;
            }
        }

        if(flag == 0){printf("소수이다. \n");}
        else{printf("소수가 아니다. \n");}

    }

END:
    return 0;
}
