#include<stdio.h>
#include<stdlib.h>
#define MAX 1001

int adj[MAX][MAX] = {0, };
int visited[MAX] = {0, };

void DFS(int v, int start);

int main(){

    int v,e;
    int x,y;

    printf("input VertexNum & EdgeNum \n");
    scanf("%d %d", &v, &e);
    printf("\n");
    printf("input Edge information \n");
    for(int i = 1; i <= e; i++){
        scanf("%d %d\n", &x, &y);
        adj[x][y] = 1;
        adj[y][x] = 1;
    }

    int start = 1;

    DFS(v, start);
}

void DFS(int v, int start){

    int temp;

    visited[start] = 1;
    printf("%d ", start);

    for(int i = 0; i <= v; i++){
        if(adj[start][i] == 1){
                temp = i;
                if(!visited[temp]){
                    DFS(v, temp);
                }
        }
    }
}

