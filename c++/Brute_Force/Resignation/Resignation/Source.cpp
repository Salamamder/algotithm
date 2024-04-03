#include <iostream>

using namespace std;
int n;
int t[21], pay[21];
int ans = 0;

void go(int day, int sum)
{
	if (day == n + 1)
	{
		if (ans < sum) ans = sum;
		return;
	}

	if (day > n + 1)
		return;

	go(day + 1, sum);
	go(day + t[day], sum + pay[day]);
}

int main()
{
	cin >> n;
	for (int i = 1; i <= n; i++)
	{
		cin >> t[i] >> pay[i];
	}

	go(1, 0);
	cout << ans << '\n';
	return 0;
}