#include <iostream>

using namespace std;

int d[1000];
int a[1000];

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n;
	cin >> n;

	for (int i = 1; i <= n; i++)
	{
		cin >> a[i];
	}

	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= i; j++)
		{
			d[i] = max(d[i], d[i - j] + a[j]);
		}
	}

	cout << d[n] << '\n';
	return (0);
}