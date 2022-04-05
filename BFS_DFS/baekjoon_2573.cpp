#include<iostream>
#include<vector>
#include<algorithm>
#include<deque>

using namespace std;
int graph[301][301] ={0, };
int new_graph[301][301] ={0, };
int drow[4] = {1,-1,0,0};
int dcol[4] = {0,0,1,-1};
int ans = 0;

void dfs(int n, int m){

    for(int row =0; row<n; row++){
        for(int col = 0; col<m; col++){
            if(graph[row][col] != 0){
                int cnt = 0;
                for(int i=0; i<4; i++){
                    int nrow = row + drow[i];
                    int ncol = col + dcol[i];
                    if(graph[nrow][ncol ] == 0){cnt++;}
                }
                new_graph[row][col] = cnt;
            }
        }
    }

    for(int row =0; row<n; row++){
        for(int col = 0; col<m; col++){
            if(graph[row][col] !=0){
                graph[row][col] = graph[row][col] - new_graph[row][col];
                if(graph[row][col] < 0){
                    graph[row][col] = 0;
                }
            }
        }
    }

    int cnt = 0;
    int check[n][m] ={0, };
    for(int row =0; row<n; row++){
        for(int col = 0; col<m; col++){
            if(graph[row][col] !=0 && check[row][col] ==0){
                cnt ++;
                deque<pair<int,int>> q;
                q.push_back({row,col});
                check[row][col] = 1;
                while(!q.empty()){
                    int r = q.front().first;
                    int c = q.front().second;
                    q.pop_front();

                    for(int i =0; i<4; i++){
                        int nrow = r + drow[i];
                        int ncol = c + dcol[i];

                        if(graph[nrow][ncol] != 0 && check[nrow][ncol] == 0){
                            check[nrow][ncol] = 1;
                            q.push_back({nrow,ncol});
                        }
                    }
                }
            }
        }
    }

    if(cnt == 1){
        ans++;
        dfs(n,m);
    }else if(cnt>1){
        ans ++;
    }else if(cnt ==0){
        ans = 0;
    }
}

int main(){

    int n,m;
    cin >> n >> m;
    for(int row = 0; row<n; row++){
        for(int col = 0; col<m; col++){
            int k;
            cin >> k;
            graph[row][col] = k;
        }
    }

    dfs(n,m);
    cout << ans << endl;
    return 0;
}

