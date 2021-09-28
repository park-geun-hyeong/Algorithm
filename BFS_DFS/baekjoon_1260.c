#include<stdio.h>

int graph[1001][1001];
int dfsvisited[1001]={0};
int bfsvisited[1001]={0};
int queue[1001];

void BFS(int v, int n){

    int front = 0;
    int rear = 0;
    int i,POP;

    queue[0] = v;
    printf("%d ", v);
    bfsvisited[v] = 1;
    rear++;

    while(front<rear){

        POP = queue[front];
        front++;

        for(i=1; i<=n; i++){
            if(graph[POP][i] == 1 && bfsvisited[i] == 0){
                queue[rear] = i;
                bfsvisited[i] = 1;
                printf("%d ", i);
                rear++;
            }

       }
    }
    return;
}

void DFS(int v, int n){

    int i;

    dfsvisited[v] = 1;
    printf("%d ", v);

    for(i=1; i<=n; i++){
        if((graph[v][i] == 1) && dfsvisited[i] == 0){
                DFS(i,n);

        }
    }
    return;
}

int main(){

    int n,m,v;
    int i,x,y;

    scanf("%d %d %d", &n, &m, &v);

    for(i=1; i<=m; i++){
        scanf("%d %d", &x, &y);
        graph[x][y] = graph[y][x] = 1;
    };


    DFS(v,n);
    printf("\n");
    BFS(v,n);

    return 0;
}


