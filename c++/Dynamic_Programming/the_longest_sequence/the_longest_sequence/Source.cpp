#include <iostream>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int a[1000];
	int d[1000];
	int n;
	int m = 0;

	cin >> n;

	for (int i = 1; i <= n; i++)
	{
		cin >> a[i];
	}

	for (int i = 1; i <= n; i++)
	{
		d[i] = 1;
		for (int j = 1; j < i; j++)
		{
			if (a[i] > a[j] && d[i] < d[j] + 1)
			{
				d[i] = d[j] + 1;
			}
		}

		if (d[i] > m)
			m = d[i];
	}
	cout << m << '\n';
	return(0);
}