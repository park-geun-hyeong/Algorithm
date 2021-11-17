#include<stdio.h>
#define num 1000000000

int main(){

    int n;
    int dp[101][10]= {};
    scanf("%d", &n);

    for(int i=1; i<10; i++){
        dp[1][i] = 1;
    }

    for(int j=2; j<n+1; j++){
        for(int k=0; k<10; k++){
            if(k == 0){
                dp[j][0] = dp[j-1][1];
            }
            else if(k == 9){
                dp[j][9] = dp[j-1][8];
            }
            else{
                dp[j][k] = dp[j-1][k-1] + dp[j-1][k+1];
            }
        }
    }

    int ans = 0;

    for(int q=0; q < 10; q++){
        ans = ans + dp[n][q];
    }

    printf("%d\n", ans%num);
    return 0;
}

