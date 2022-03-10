#include<stdio.h>
#include<vector>
#include<algorithm>

using namespace std;

int main(){

    int n;
    scanf("%d",&n);
    vector<int> v;
    int j;
    for(int i = 0 ; i < n; i++){
        scanf("%d",&j);
        v.push_back(j);
    }

    sort(v.begin(), v.end());

    for(int i = 0; i < n; i++){
        printf("%d",v[i]);
        printf("\n");
    }
    return 0;
}

