#include<stdio.h>

int max(int a, int b){
    return a>b ? a:b;
};


int main(){
    int n;
    int j;

    scanf("%d", &n);

    int arr[301];
    for(j=1; j<=n; j++){
        scanf("%d", &arr[j]);
    }

    int i;
    int dp[301];

    for(i=1; i<=n; i++){
        if(i == 1 ){
           dp[i] = arr[i];
        }
        else if(i == 2){
            dp[i] = max(arr[i-1] + arr[i], arr[i]);

        }
        else if(i==3){
            dp[i]  = max(arr[i-1] + arr[i], arr[i-2] + arr[i]);

        }
        else{

            dp[i] = max(arr[i] + dp[i-2], arr[i] + arr[i-1] + dp[i-3]);
        }

    }

    int m = dp[n];
    printf("%d", m);

};

