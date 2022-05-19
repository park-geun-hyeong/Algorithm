#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>
#define INF 1e9

using namespace std;

int main(){

    int n,m,x;
    cin >> n >> m >> x;
    vector<pair<int, int>> linked_list[n+1];

    for(int i = 0; i<m; i++){
        int s,e,t;
        cin >> s >> e >> t;
        linked_list[s].push_back({e,t});
    }



    int paths[n+1][n+1] = {0,};
    for(int start = 1; start<n+1; start++){
        for(int node = 1; node <n+1; node ++){
            if(node == start){
                paths[start][node] = 0;
            }else{
                paths[start][node] = INF;
            }

        }

        priority_queue<pair<int, int>, vector<pair<int,int>>, greater<pair<int,int>>> q;
        q.push({0, start});

        while(!q.empty()){
            int current_distance = q.top().first;
            int current_dst = q.top().second;
            q.pop();

            if(paths[start][current_dst] < current_distance){
                continue;
            }

            for(int i = 0; i < linked_list[current_dst].size(); i++){
                int next_dst = linked_list[current_dst][i].first;
                int next_distance = linked_list[current_dst][i].second;
                int NEW = current_distance + next_distance;

                if(NEW < paths[start][next_dst]){
                    paths[start][next_dst] = NEW;
                    q.push({NEW, next_dst});
                }
            }
        }
    }

    int ans = -1;
    for(int i = 1;i<n+1;i++){
        int d = paths[i][x] + paths[x][i];
        if(d>ans){
            ans = d;
        }
    }

    cout<<ans<<endl;
    return 0;

