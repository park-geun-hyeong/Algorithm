#include<stdio.h>

graph[26][26];
dx[4]={1,-1,0,0};
dy[4]={0,0,1,-1};
int apart[26*26] ={0};
int cnt = 0;
int n = 0;
int result = 0;


int dfs(int x, int y){
    int i,nx,ny;

    if(x<=0 || x>n || y<=0 || y>n){
        return 0;
    }

    if(graph[x][y] == 1){
        graph[x][y] = 0;
        cnt++;

        for(i=0; i<4; i++){
            nx = x + dx[i];
            ny = y + dy[i];
            dfs(nx, ny);
            }

        return 1;
        }
    return 0;
}

int main(){

    int i,j;
    scanf("%d",&n);

    for(i=1; i<=n; i++){
        for(j=1; j<=n; j++){
            scanf("%1d", &graph[i][j]);
        }
    }


    for(i=1; i<=n; i++){
        for(j=1; j<=n; j++){
            if(dfs(i,j) == 1){
                apart[cnt]++;
                result++;
                cnt = 0;

            }
        }
    }

    int k;

    printf("%d",result);
    printf("\n");
    for(k=0; k<26*26; k++){
        if(apart[k] != 0){
            int q = apart[k];
            for(int j = 0; j < q; j++) {
                printf("%d\n", k);
            }
        }
    }

    return 0;

};

