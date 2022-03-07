#include<iostream>
#include<vector>
#define inf 1e9

int graph[101][101];
int path[101][101] ={0, };

int main(){
    int n, m;
    std::cin >> n >> m;


    for(int i = 1; i<=n; i ++){
        for(int j = 1; j<=n; j++){
            if(i == j){
                graph[i][j] = 0;
            }
            else{graph[i][j] = inf;}
        }
    }

    for(int i = 1; i <= m; i++){
        int a,b,c;
        std::cin >> a >> b >> c;
        if(graph[a][b] > c){
            graph[a][b] = c;
            path[a][b] = a;
        }
    }

    for(int Mid = 1; Mid <= n; Mid++){
        for(int Start = 1; Start <= n; Start++){
            if(Start == Mid) continue;
            for(int End = 1; End <= n; End++){
                if(End == Mid) continue;
                if(graph[Start][End] > graph[Start][Mid] + graph[Mid][End]){
                    graph[Start][End] = graph[Start][Mid] + graph[Mid][End];
                    path[Start][End] = path[Mid][End];
                }
            }
        }
    }

    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n; j++){
            if(graph[i][j] == inf){
                std::cout << 0 << " ";
            }
            else{
                std::cout << graph[i][j] << " ";
            }
        }
        std::cout << "\n";
    }

    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n; j++){
            if(graph[i][j] == inf || i==j){
                std::cout << 0 <<std::endl;
            }
            else{
                std::vector<int> ans;
                ans.push_back(j);
                int cur = j;
                while(cur != i){
                    ans.push_back(path[i][cur]);
                    cur = path[i][cur];
                }
                std::cout << ans.size() << " ";
                for(int k = ans.size() - 1; k >= 0; k--){
                    std::cout<<ans[k] << " ";
                }
                std::cout<<"\n";
            }
        }
    }

    return 0;

}

