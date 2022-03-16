#include<iostream>
#include<vector>
#include<algorithm>
#include<deque>
#include<string>
#include<cmath>

using namespace std;
int state[4][8] ={0,};

void moving(int direction, int row){
    if(direction == 1){
        int temp = state[row][7];
        for(int i = 7; i > 0; i--){
            state[row][i] = state[row][i-1];
        }
        state[row][0] = temp;
    }else{
        int temp = state[row][0];
        for(int i = 0; i < 7; i++){
            state[row][i] = state[row][i+1];
        }
        state[row][7] = temp;
    }
}

int opp(int direction){
    if(direction == 1){return -1;}
    else{return 1;}
}

vector<pair<pair<int, int>, pair<int, int>>> Find(int row){

    vector<pair<pair<int, int>, pair<int, int>>> ans;
    if(row == 0){
        ans.push_back({{row, 2}, {row+1,6}});
    }
    if(row == 3){
        ans.push_back({{row, 6}, {row-1,2}});
    }

    if(row == 1 || row == 2){
        ans.push_back({{row, 6},{row-1,2}});
        ans.push_back({{row, 2},{row+1,6}});
    }
    return ans;
}

int main(){

    for(int i = 0; i<4; i++){
        string row;
        getline(cin,row);
        for(int j=0; j<8; j++){
            state[i][j] = row[j] - '0';
        }
    }
//    for(int row =0; row<4; row++){
//        for(int col =0; col<8; col++){
//            cout<< state[row][col]<<" ";
//        }
//        cout<<"\n";
//    }

    int k;
    cin >> k;
    vector<pair<int, int>> method;
    for(int i =0 ; i<k; i++){
        int n,d;
        cin>>n>>d;
        method.push_back({n,d});
    }

    for(int i = 0; i<k; i++){
        int row = method[i].first;
        int direction = method[i].second;

        int order[4][2] = {0,};
        order[row-1][0] = 1;
        order[row-1][1] = direction;
        int visit[4] = {0, };
        deque<pair<int, int>> q;
        q.push_back({row-1, direction});

        while(!q.empty()){
            int num = q.front().first;
            int d = q.front().second;
            q.pop_front();
            visit[num] = 1;

            vector<pair<pair<int, int>, pair<int, int>>> beside;
            beside = Find(num);
            int length = beside.size();

            for(int i = 0; i<length; i++){
                int me = beside[i].first.first;
                int my_loc = beside[i].first.second;
                int you = beside[i].second.first;
                int your_loc = beside[i].second.second;


                if(visit[you] == 0){
                    if(state[me][my_loc] == state[you][your_loc]){
                        visit[you] = 1;
                        continue;
                    }else{
                        order[you][0] = 1;
                        order[you][1] = opp(d);
                        q.push_back({you, opp(d)});
                    }
                }
            }
        }

        for(int j = 0 ; j<4; j++){
            if(order[j][0] == 1){
                moving(order[j][1], j);
            }
        }
    }


    int score = 0;
    for(int k =0; k<4; k++){
        if(state[k][0] == 0){
            continue;
        }else{
            score = score + pow(2,k);
        }
    }

    cout<< score <<endl;
    return 0;
}

