#include <iostream>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int a[100000];
	int d[100000];
	int n;


	cin >> n;

	for (int i = 1; i <= n; i++)
	{
		cin >> a[i];
	}

	d[1] = a[1];
	int m = d[1];
	for (int i = 2; i <= n; i++)
	{
		d[i] = a[i];
		if (d[i] < d[i - 1] + a[i])
			d[i] = d[i - 1] + a[i];
		if (d[i] > m)
			m = d[i];
	}

	cout << m << '\n';
	return(0);
}