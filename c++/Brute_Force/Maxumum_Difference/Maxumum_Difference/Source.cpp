#include <iostream>
#include <algorithm>
#include<vector>

using namespace std;

int calculate(vector<int> a, int n)
{
	int ans = 0;
	for (int i = 0; i < n-1; i++)
	{
		ans += abs(a[i] - a[i + 1]);
	}
	return ans;
}

int main()
{
	int n;
	cin >> n;

	vector<int> a(n);
	for (int i = 0; i < n; i++)
	{
		cin >> a[i];
	}

	sort(a.begin(), a.end());

	int ans = 0;

	do {
		int temp = calculate(a, n);
		ans = max(ans, temp);
	} while (next_permutation(a.begin(), a.end()));

	cout << ans << '\n';
	return 0;
}