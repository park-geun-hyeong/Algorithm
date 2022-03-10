#include<iostream>
#include<vector>
#include<algorithm>
#include<deque>
#include<string>
#include<tuple>

using namespace std;
int matrix[129][129] = {0,};
int drow[4] = {1,-1,0,0};
int dcol[4] = {0,0,1,-1};

void bfs(int row, int col, int color, int h, int w){

    deque<pair<int, int>> Deque;
    Deque.push_back({row,col});
    int first_color = matrix[row][col];
    matrix[row][col] = color;

    while(!Deque.empty()){
        int Row = Deque.front().first;
        int Col = Deque.front().second;
        Deque.pop_front();

        int nrow, ncol;
        for(int i = 0; i<4; i++){
            nrow = Row + drow[i];
            ncol = Col + dcol[i];

            if(0<nrow<=h && 0<ncol<=w && matrix[nrow][ncol] == first_color){
                matrix[nrow][ncol] = color;
                Deque.push_back({nrow, ncol});
            }
        }
    }
}

int main(){

    int h,w,q;
    cin>>h>>w;

    int row = 1;
    int col = 1;
    for(int row = 1; row<=h; row ++){
        for(int col = 1; col<=w; col++){
            cin>>matrix[row][col];
        }
    }

    cin>>q;

    vector<tuple<int, int, int>> Q;
    for(int t = 0; t<q; t++){
        int i,j,c;
        cin>>i>>j>>c;
        if(matrix[i][j] != c){
            bfs(i,j,c,h,w);
        }else{continue;}
    }

    for(int row = 1; row<=h; row++){
        for(int col = 1; col<=w; col++){
            cout<< matrix[row][col]<<" ";
        }
        cout<<"\n";
    }
    return 0;
}

