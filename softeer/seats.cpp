#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>
#include<map>

using namespace std;

int matrix[21][21] = {0, };
int drow[4] = {1,-1,0,0};
int dcol[4] = {0,0,1,-1};
int check[10001] ={0,};
map<int, pair<int,int>> now_seat;

int get_safety(int row, int col,int n, int m){
    int ans = 1e9;
    for(int x = 1; x<=n; x++){
        for(int y=1;y<=m;y++){
            if(matrix[x][y] == 1){
                int safety = sqrt(pow(row-x,2) + pow(col-y,2));
                if(safety<ans){ans=safety;}
            }
        }
    }
    return ans;
}

pair<int,int> get_seat(int n,int m){

    pair<int,int> ans;
    bool zero = true;
    for(int row = 1; row<=n; row++){
        for(int col = 1; col<=m; col++){
            if(matrix[row][col] == 1){
                zero = false;
                break;
            }
        }
    }

    if(zero){
        ans.first = 1;
        ans.second = 1;
        return ans;
    }

    vector<pair<pair<int,int>, int>> cand;

    int MAX_safety = -1;
    for(int row = 1; row<=n; row++){
        for(int col = 1; col<=m; col++){
            if(matrix[row][col] == 0){
                bool seat_check = true;
                for(int i =0; i<4; i++){
                    int nrow = row + drow[i];
                    int ncol = col + dcol[i];
                    if(nrow<1 || nrow>n || ncol<1 || ncol>m){continue;}
                    if(matrix[nrow][ncol] == 1){
                        seat_check = false;
                        break;
                        }else{continue;}
                    }
                if(seat_check){
                    int safety = get_safety(row,col,n,m);
                    if(safety > MAX_safety){
                        MAX_safety = safety;
                    }
                    cand.push_back({{row,col}, safety});
                }
            }
        }
    }

    if(cand.size() == 0){
        ans.first = 0;
        ans.second = 0;
        return ans;
    }

    vector<pair<int, int>> new_cand;
    for(int i =0; i<cand.size(); i++){
        if(cand[i].second == MAX_safety){
            new_cand.push_back({cand[i].first.first, cand[i].first.second});
        }
    }

    if(new_cand.size()>1){
        sort(new_cand.begin(), new_cand.end());
    }
    return new_cand[0];
}

int main(){

    int n,m,q;
    cin>>n>>m>>q;
    string state;
    int id;
    vector<pair<string, int>> work;
    for(int i = 0; i<q; i++){
        cin >> state >> id;
        work.push_back({state, id});
    }

    for(int i = 0; i<q; i++){
        state = work[i].first;
        id = work[i].second;

