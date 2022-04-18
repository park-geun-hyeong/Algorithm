#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(int argc, char** argv)
{	

	int n;
	cin >> n;
	vector<pair<int, int>> times;
	for(int i = 0; i<n ;i++){
		int s,e;
		cin >> s >> e;
		times.push_back({e,s});
	}

	sort(times.begin(), times.end());

	int cnt = 0;
	int now_end = 0;
	for(int i = 0 ; i<n; i++){
		int end, start;
		end = times[i].first;
		start = times[i].second;

		if(start >= now_end){
			cnt ++;
			now_end = end;
		}
	}

	cout << cnt << endl;
	return 0;
}
