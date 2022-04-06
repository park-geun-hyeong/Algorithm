#include<iostream>
#include<vector>
#include<algorithm>
//#define max(a,b) (((a)>(b)) ? (a) : (b))

using namespace std;
int graph[501][501]={0,};
int dp[501][501]={0,};
int dp_check[501][501]={0,};
int check[501][501]={0,};
int drow[4] ={1,-1,0,0};
int dcol[4] ={0,0,1,-1};
int MAX = 0;

int dfs(int n, int row ,int col){
    dp_check[row][col] = 1;

    int num = graph[row][col];

    for(int i=0; i<4; i++){
        int depth = 1;
        int nrow = row + drow[i];
        int ncol = col + dcol[i];

        if(0<=nrow<n && 0<=ncol<n){
            if(graph[nrow][ncol] >num && check[nrow][ncol] == 0){
                if(dp_check[nrow][ncol] == 1){
                    dp[row][col] = max(dp[row][col], depth+dp[nrow][ncol]);
                }else{
                    check[nrow][ncol] = 1;
                    int cnt = dfs(n,nrow,ncol);
                    check[nrow][ncol] = 0;
                    depth = depth+ cnt;
                    dp[row][col] = max(dp[row][col], depth);
                }
            }
        }

    }

    return dp[row][col];
}


int main(){

   int n;
   cin >> n;


    for(int row =0; row<n; row++){
        for(int col= 0; col<n; col++){
            int a;
            cin >> a;
            graph[row][col] = a;
            dp[row][col] = 1;
        }
    }
//    for(int row =0; row<n; row++){
//        for(int col= 0; col<n; col++){
//            cout <<dp[row][col] << " ";
//        }
//        cout<< "\n";
//    }

    for(int row =0; row<n; row++){
        for(int col= 0; col<n; col++){
            if(dp_check[row][col] == 0){
                check[row][col] = 1;
                dfs(n,row,col);
                check[row][col] = 0;
            }
            MAX = max(MAX, dp[row][col]);
            }
        }

    cout << MAX << endl;
    return 0;

}

