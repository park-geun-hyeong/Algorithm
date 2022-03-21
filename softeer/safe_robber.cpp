#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(int argc, char** argv)
{	
	int w, n;
	cin >> w >> n;
	vector<pair<int, int>> price;
	for(int i = 0; i <n; i++){
		int m,p;
		cin >> m >> p;
		price.push_back({p,m});
	}

	sort(price.rbegin(), price.rend());

	int residual = w;
	int ans = 0;
	for(int i = 0; i < n; i ++){
		int p = price[i].first;
		int m = price[i].second;
		if(residual <= m){
			ans = ans + residual*p;
			break;
		}
		ans = ans + m*p;
		residual = residual - m;
	}

	cout << ans << endl;

	return 0;
}
